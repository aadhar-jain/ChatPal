import random
from logic1 import *
from logic2 import *
from logic3 import *
from logic4 import *

from time import sleep
import sys
encrypted_string=""

def calc_logic(raw_letter):
    # random logic no , then apply that logic, append to global string
    global encrypted_string
    logic=random.randint(1,4)
    if logic==1:
        encrypted_string = encrypted_string+ logic_one(raw_letter)
    elif logic==2:
        encrypted_string = encrypted_string+ logic_two(raw_letter)
    elif logic==3:
        encrypted_string = encrypted_string+ logic_three(raw_letter)
    else:
        encrypted_string = encrypted_string+ logic_four(raw_letter)

    return

def into_letters(raw_line):
    global encrypted_string
    for raw_letter in raw_line:
        # space between words daalni pdgi yha
        if raw_letter==" ":
            encrypted_string=encrypted_string+chr(10000)
        else:
            calc_logic(raw_letter)
    # add krna h string mein unicode for line change ,, for ke bahar
    encrypted_string = encrypted_string + chr(10001)
    return

def takeline():
    # considering maximum msg to be encrypted will be of 100 lines
    for line_no in range(1,101,1):
        # raw=""
        raw=input()
        # condition to check if quit is entered, if yes ,
        # whatever is encrypted in global string till now is printed
        if(raw.lower()=="quit"):
            print("Your encrypted data is :--")
            for t in encrypted_string:
                print(t,end="")
                sleep(random.uniform(0,0.3))
            print()
            print()
            return
        else:
            into_letters(raw)
    # encryption line by line i.e input a line and encrypt it directly
    # then input second line


# main body start
response_msg="ACCESS GRANTED..."
password=input("Enter password to access : ")
if(password=="permitE"):
    # for just typewriter effect
    for w in response_msg:
        print(w,end="")
        sys.stdout.flush()
        sleep(0.1)
    print()
    print()
    print("Enter data to Encrypt :-")
    #start taking msg to encrypt
    takeline()
else:
    print("ACCESS DENIED!")