from addbook import *
from search import *
from update import *

print("choose option that you want to use:")
while True:
    print(" for search book press 1\n","for update status of book press 2\n","for add book press 3\n", "for exit prees 4")
    choice=input("please make your choice:")
    while choice not in ["1","2","3","4",1,2,3,4]:
            choice=input("wrong input, please enter an existing menu number:")
    else: pass


    if choice=="1" :search()
    elif choice=="2" : update()
    elif choice=="3" : addbook()
    elif choice=="4" :
        print("you choose exit, if you want to make any other operation please restart the app.")
        exit()

    cont = input("would you like to do any other operation? Y/N :")
    while cont not in "YyNn":
        cont = str(input('Wrong choice! Do you wish to continue? [Y/N] ')).upper()[0]
    if cont in 'Nn':
        break