from random import *
def ran_pass():
    """The program will generate a random password.
    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    psword = ''.join([random.choice(ls) for x in range(12)])
    print(psword)
def pas_check():
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
        print("Minimum 6 chracters!")
    elif up >= 0 and low >= 0 and symb >= 0 and num >= 0:
        print("Good password")
    else:
        print("Too weak password")
