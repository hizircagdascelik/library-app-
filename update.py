def update():
    import pickle

    a_file=open("lib_data.txt","rb")
    booklist=pickle.load(a_file)
    find=input("input a book name which will be updated:").strip().title()


    for i in range(0,len(booklist)):
            if find in booklist[i].values():

                print("this book will be updated",booklist[i])
                booklist[i].update({"Status":input("new status")})
                while booklist[i]["Status"] != 'A' and booklist[i]["Status"] != 'U':
                    booklist[i]["Status"] = str(input('Wrong choice! Status: [A/U]')).upper()[0]
                print("updated",booklist[i])
                a_file=open("lib_data.txt","wb")
                pickle.dump(booklist,a_file)


    a_file = open("lib_data.txt","rb")
    booklist=pickle.load(a_file)
    print("new list",booklist)





    a_file.close()