from getpass import getpass
import crypton

def view():

    with open('passwords.txt', 'r') as po:
       for line in po.readlines():
        data = line.rstrip()
        user, acctype, passw = data.split("|")
        print(f'Username: {user} ,Type of Acc: {acctype} ,Password: {crypton.decrypt(passw)}')

def add():
    
    user_name = input('Enter USERNAME: ')
    type_acc = input('Enter TYPE of account this is: ')
    password = getpass('Enter PASSWORD: ')

    with open('passwords.txt', 'a') as po:
        po.write(user_name+"|"+type_acc+"|"+crypton.encrypt(password)+"\n")


