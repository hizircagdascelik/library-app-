def search():
# search part of the code, we try to check each list element which has same "name" variable with input
    import pickle

    src_book=input("input a book name for search:").strip().title()
    itr=0
    a_file=open("lib_data.txt","rb")

    search=pickle.load(a_file)
    sorted_search = sorted(search, key = lambda p: p['name'])
    for i in range(0,len(search)):

            if src_book in sorted_search[i].get("name"):# malath--- malath sth works once, malath----malath sth malath sth malath works 3 times
                print("we have books which contains",src_book,end="/")
                print(sorted_search[i])
                a_file.close()
                itr += 1

    if itr == 0 : print("no we dont have that boook!")

    a_file.close()