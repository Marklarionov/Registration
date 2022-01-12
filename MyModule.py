from random import*
login=["m","lol"]
psword=["rrrrrr6R","lollol6L"]
def registr():
    """ Registers a user in the system.Requests username and password.
    """
    log=input("Login: ")
    if log in login:
        print("This username already exists, please use another.")
        try:
            log=input("Login: ")
        except:
            print("This username already exists, please use another.")
    log.join(login)
    print(login)
    print("You want to create a password yourself or take a random one(1 or 2)")
    ans1=int(input())
    if ans1==1:
        print("You need minimum 6 characters, at least 1 number and 1 capital letter")
        print("Please,write down your password")
        pas=input()
        print(pas_check())
        pas.join(psword)
    elif ans1==2:
        print("Password is being generated.")
        print(ran_pass())
        print("Remember this password.")
    else:
        print("Error")

def log_in():
    """ Authorizes the user using login and password.
    """
    print("Write your Login.")
    log1=input("")
    login.index(log1)
    if log1 in login:
        print("Write your password.")
        pas1=input()
        if pas1 in psword:
            print("You are successfully logged in!")

def ran_pass():
    pass
    """The program will generate a random password.
    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    shuffle(ls)
    psword = ''.join([choice(ls) for x in range(12)])
    print(psword)

def pas_check():
    pass
    """Write down your password and computer check his difficult.
    """
    for i in pas:
        up=0
        low=0
        symb=0
        num=0 
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
        elif i.isdigit():
             num += 1
        else:
             symb += 1
    if len(pas) <= 6:
        print("Minimum 6 characters!")
    elif up >= 0 and low >= 0 and symb >= 0 and num >= 0:
        print("Good password")
    else:
        print("Too weak password")
