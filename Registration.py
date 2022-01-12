from MyModule import*
from random import*
login=["m","lol"]
psword=["rrrrrr6R","lollol6L"]
while 1:
    print("Registration or Authorization or Exit?(1 or 2 or 3)")
    ans=int(input())
    if ans==1:
        print(registr())
    elif ans==2:
        print(log_in())
    elif ans==3:
        print("Have a nice day!")
        break
    else:
        print("incorrect value")
