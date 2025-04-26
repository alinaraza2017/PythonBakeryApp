#using the concepyt of string
a='Welcome to ELITE BAKERS!'
print(a)


#using the function concept to define the login and then using the while loop and if statements to make the yser input the correct info
def login():
    email_address=input("enter your email address \nexample@gmail.com")
    while "@" not in email_address:
      email_address = input("Your email address must have '@' in it\nPlease write your email address again: ")
    if len(email_address) <= 6 :
        email_address = input("Your email address is too short\nPlease write your email address again: ")
    if "." not in email_address:
        email_address = input("Your email address must have '.' in it\nPlease write your email address again: ")
    pswrd=input("enter your password\n It must be atleast 8 characters long")
    if len(pswrd)<=8:
        pswrd= input("please re-enter your password")
    if len(pswrd)>12:
        pswrd= input("please re-enter your password")
        


#using the function concept to define the signup and then using the while loop and if statements to make the yser input the correct info
def signup():
    name=input("enter your full name")
    email_address=input("enter your email address \nexample@gmail.com")
    while "@" not in email_address:
      email_address = input("Your email address must have '@' in it\nPlease write your email address again: ")
    if len(email_address) <= 6 :
        email_address = input("Your email address is too short\nPlease write your email address again: ")
    if "." not in email_address:
        email_address = input("Your email address must have '.' in it\nPlease write your email address again: ")
    pswrd=input("enter your password\n It must be atleast 8 characters long")
    if len(pswrd)<=8:
        pswrd= input("please re-enter your password")
    if len(pswrd)>12:
        pswrd= input("please re-enter your password")
    city=input("choose your city:\n a)Islamabad \n b)Rawalpindi \n c)Lahore")
    phonenum=input("enter your phone number")
    num=phonenum.split("-")
    area=num[0]
    while area.isdigit() == False :
        phonenum=input("Number: ")
        num=phonenum.split("-")
        area=num[0]
    if len(phonenum)>11:
        phonenum=input("please re-enter your phone number")
        while area.isdigit() == False :
            phonenum=input("Number: ")
            num=phonenum.split("-")
            area=num[0]
    if len(phonenum)<11:
        phonenum=input("please re-enter your phone number")
        while area.isdigit() == False :
            phonenum=input("Number: ")
            num=phonenum.split("-")
            area=num[0]

#using the while loop and if statements, calling the functions, and using break to break the loop. 
while (a):
 accountstatus=input("choose: a)login  b)sign up  c)exit")
 if accountstatus=="a":
     login()
     print("Welcome back! \n enjoy shopping")
     import os
     os.system("menu.py")
 if accountstatus=="b":
     signup()
     print("Hey there! \n Thanks for joining. We’re thrilled to have you.")
     import os
     os.system("menu.py")
 if accountstatus=="c":
     break






















