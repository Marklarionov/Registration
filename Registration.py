import random
length=0
login=[]
psword=[]
while 1:
    print("Registration or Authorization?(1 or 2)")
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
