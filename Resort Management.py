import mysql.connector
import datetime
global z
mydb = mysql.connector.connect(user='root', password='root', host='localhost', database='resort')
mycursor=mydb.cursor()
print("Welcome to Royal Heritage resort:")
def registercust():
     L=[]
     custname=input("enter name:")
     L.append(custname)
     addr=input("enter address:")
     L.append(addr)
     indate=input("enter check in date:")
     L.append(indate)
     outdate=input("enter check out date:")
     L.append(outdate)
     custdata=(L)
     sql="insert into custdata(custname,addr,indate,outdate)values(%s,%s,%s,%s)"
     mycursor.execute(sql,custdata)
     mydb.commit()
def roomtypeview():
    print("Do you want to see room type available ? ")
    print("Enter 1 for yes:")
    ch=int(input("enter your choice:"))
    if ch==1:
         sql="select * from roomtype"
         mycursor.execute(sql)
         rows=mycursor.fetchall()
         for x in rows:
              print(x)
def roomrent():
     print ("We have the following rooms for you:-")
     print ("1. DELUXE=Rs 1000 PN\-")
     print ("2. PREMIUM=Rs 2000 PN\-")
     print ("3. EXECUTIVERs 3000 PN\-")
     print ("4. ROYAL Rs 4000 PN\-")
     x=int(input("Enter Your Choice Please->"))
     n=int(input("How Many Nights Will You Stay:"))
     if(x==1):
          print ("you have opted for DELUXE room type ")
          s=1000*n
     elif (x==2):
          print ("you have opted for PREMIUM  room type ")
          s=2000*n
     elif (x==3):
          print ("you have opted for EXECUTIVE room type ")
          s=3000*n
     elif (x==4):
          print ("you have opted for ROYAL room type ")
          s=4000*n
     else:
          print ("please choose a room")
     print ("your room rent is =",s,"\n")
def restaurantmenuview():
      print("Do you want to see menu available :")
      print("enter 1 for yes:")
      ch=int(input("enter your choice:"))
      if ch==1:
           sql="select * from restaurant"
           mycursor.execute(sql)
           rows=mycursor.fetchall()
           for x in rows:
                print(x)
def orderitem():
     global s
     ch=int(input("enter your choice:"))
     if ch==1:
          sql="select * from restaurant"
          mycursor.execute(sql)
          rows=mycursor.fetchall()
          for x in rows:
               print(x)          
     print("Please select from above list:")
     d=int(input("enter your choice:"))
     if(d==1):
          print("you have ordered tea:")
          a=int(input("enter quantity:"))
          s=10*a
          print("your amount for tea is :",s,"\n")
     elif (d==2):
          print("you have ordered coffee:")
          a=int(input("enter quantity:"))
          s=10*a
          print("your amount for coffee is :",s,"\n")
     elif(d==3):
          print("you have ordered a softdrink:")
          a=int(input("enter quantity:"))
          s=20*a
          print("your amount for softdrink is :",s,"\n")
     elif(d==4):
          print("you have ordered samosa:")
          a=int(input("enter quantity:"))
          s=15*a
          print("your amount for samosa is :",s,"\n")
     elif(d==5):
          print("you have ordered sandwich: ")
          a=int(input("enter quantity:"))
          s=50*a
          print("your amount for sandwich is :",s,"\n")
     elif(d==6):
          print("you have ordered wafers:")
          a=int(input("enter quantity:"))
          s=30*a
          print("your amount for  wafers is  :",s,"\n")
     elif(d==7):
          print("you have ordered ice cream: ")
          a=int(input("enter quantity:"))
          s=20*a
          print("your amount for  ice cream is :",s,"\n")
     elif(d==8):
          print("you have ordered milk:")
          a=int(input("enter quantity:"))
          s=20*a
          print("your amount for milk is :",s,"\n")
     elif(d==9):
         print("you have ordered water: ")
         a=int(input("enter quantity:"))
         s=50*a
         print("your amount for water  is :",s,"\n")   
     elif(d==10):
         print("you have ordered pasta:")
         a=int(input("enter quantity:"))
         s=100*a
         print("your amount for pasta is :",s,"\n")
     else:
         print("please enter your choice from the menu")
def laundarybill():
     global z
     print("enter 1 :")
     ch=int(input("enter your choice:"))
     if ch==1:
          sql="select * from laundary"
          mycursor.execute(sql)
          rows=mycursor.fetchall()
          for x in rows:
               print(x)
     y=int(input("enter number of clothes:"))
     z=y*50
     print("your laundary bill is:",z,"\n")
     return z
def Menuset():
     print("enter 1: To enter customer data")
     print("enter 2 : To view roomtype")
     print("enter 3 : for calculating room bill")
     print("enter 4 : for viewing restaurent menu")
     print("enter 5 : for restaurant bill")
     print("enter 6 :for laundary bill")
     print("enter 7: for exit:")
     try:
          userinput=int(input("please select an above option:"))
     except ValueError:
          exit("\n hi thats not a number")
          userinput=int(input("enter your choice"))
     if(userinput==1):
        registercust()
     elif(userinput==2):
        roomtypeview()
     elif(userinput==3):
        roomrent()
     elif (userinput==4):
        restaurantmenuview()
     elif(userinput==5):
        orderitem()
     elif(userinput==6):
        laundarybill()
     elif(userinput==7):
          quit()
     else:
          print("enter correct choice:")
Menuset()
