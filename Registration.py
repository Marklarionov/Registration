from MyModule import*
from random import*
login=[""]
psword=[""]
while 1:
    print("Registration or Authorization or Exit?(1 or 2 or 3)")
    ans=int(input())
    if ans==1:
        print(registr(login,psword))
    elif ans==2:
        print(log_in(login,psword))
    elif ans==3:
        print("Have a nice day!")
        break
    else:
        print("incorrect value")
