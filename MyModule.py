from random import*

def failist_lugemine(f:str,l:list):
    """
    """
    fail=open(f,"r") #,enconding"utf-8-sig"
    for rida in fail:
        l.append(rida.strip())#"\n"
    fail.close()
    return l

def fail_salv(f:str,l:list):
    """
    """
    fail=open(f,"w")
    for el in l:
        fail.write(el+"\n")
    fail.close()

def rida_salvestamine(f:str,rida:str):
    """Üks sõna või lause(rida) salvestamine
    failisse
    :param str f: fail kuku salvestame
    :param str rida: sõna, mis vaja salvestada failisse
    """
    fail=open(f,"a")
    fail.write(rida+"\n")
    fail.close()



def registr(login:list,psword:list):
    """Registers a user in the system.Requests username and password.
    """
    log=input("Login: ")
    if log in login:
        print("This username already exists, please use another.")
        try:
            log=input("Login: ")
        except:
            print("This username already exists, please use another.")
    login=list(log)
    print(rida_salvestamine("logins.txt",log))
    print(login)
    print("You want to create a password yourself or take a random one(1 or 2)")
    ans1=int(input())
    if ans1==1:
        print("You need minimum 6 characters, at least 1 number and 1 capital letter")
        print("Please,write down your password")
        pas=input()
        print(pas_check(pas))
        psword=list(pas)
    elif ans1==2:
        print("Password is being generated.")
        print(ran_pass())
    else:
        print("Error")

def log_in(login:list,psword:list):
    """ Authorizes the user using login and password.
    """
    global log
    if log in login:
        print("Write your Login.")
        log=input("")
        login.index(log1)
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
    pasword = ''.join([choice(ls) for x in range(12)])
    psword=list(pasword)
    print(pasword)

def pas_check(pas:str):
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
