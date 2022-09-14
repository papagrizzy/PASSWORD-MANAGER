import time
import os
from getpass import getpass
import dependancy as dep
import crypton


if os.stat("key.txt").st_size==0:
    print("Welcome USER!")
    time.sleep(1)
    print("Looks like it's your first time!")
    print("To access your passwords, you require a MASTERPASSWORD.")
    print("This MASTERPASSWORD will be created once and cannot be changed.")
    choice = input("Create your MASTERPASSWORD?(y/n): ").lower()

    if choice == "n":
        print("Quitting program....")
        quit()
    
    master_pwd = getpass("Enter new MASTERPASSWORD: ")
    test = getpass("Enter MASTERPASSWORD again: ")

    while master_pwd != test:

        print("Previous MASTERPASSWORD does not match!")
        print("Try again!")
        master_pwd = getpass("Enter new MASTERPASSWORD: ")
        test = getpass("Enter MASTERPASSWORD again: ")
    
    with open('key.txt', 'a') as f:
        f.write(crypton.encrypt(master_pwd))
    print("MASTERPASSWORD saved successfully!")
    print("Looks like we are good to go.")


master_pwd = getpass("Type in the MASTERPASSWORD to enter: ")
with open('key.txt') as k:
    passw_list = k.readlines()
    passw_d = passw_list[0]

run = "y"

while master_pwd != crypton.decrypt(passw_d) and run == "y":
    print("Wrong Password!")
    run = input("Do you want to try again?(y/n)").lower()
    master_pwd = getpass("Type in the MASTERPASSWORD to enter: ")


while True:

    user_dec = input("Enter ADD or VIEW or QUIT: ").upper()

    if user_dec == "QUIT":
        print("Quitting Program....")
        quit()

    if user_dec == "ADD":
        dep.add()

    elif user_dec == "VIEW":
        dep.view()

    else:
        print("Invalid input!!")
        print("Try again!!")
        continue

