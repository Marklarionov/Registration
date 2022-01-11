import random
from MyModule import *
length=0
login=["m"]
psword=["rrrrrr6R"]
while 1:
    print("Registration or Authorization or Exit?(1 or 2 or 3)")
    ans=int(input())
    if ans==1:
        log=input("Login: ")
        log.join(login)
        print("You want to create a password yourself or take a random one(1 or 2)")
        ans1=int(input())
        if ans1==1:
            print("You need minimum 6 characters, at least 1 number and 1 capital letter")
            print("Please,write down your password")
            pas=input()
            print(pas_check)  
            pas.join(psword)
        elif ans1==2:
            print("Password is being generated.")
            print(ran_pass)
            print("Remember this password.")
        else:
            print("Error")
    elif ans==2:
        print("Write your Login.")
        log1=input("")
        if log1 in login:
            print("Write your password.")
            pas1=input()
            if pas1 in psword:
                print("You are successfully logged in!")
    elif ans==3:
        print("Have a nice day!")
    else:
        print("Error")
