def addbook():

    import pickle

    try:
        book = {}
        a_file=open("lib_data.txt", "rb")
        library = list(pickle.load(a_file))
    except:
        book={}
        library=[]


    while True:
        book['name'] = str(input('\nInput book name: ')).strip().title()
        book['author'] = str(input('Input author: '))
        book['category'] = str(input('Input category: '))
        book['Status'] = str(input('Status: [A/U] ')).strip().upper()[0]
        while book['Status'] != 'A' and book['Status'] != 'U':
            book['Status'] = str(input('Wrong choice! Status: [A/U]')).upper()[0]
        library.append(book.copy())


        cont = str(input('Do you wish to continue? [Y/N] ')).upper()[0]
        while cont != 'Y' and cont != 'N':
            cont = str(input('Wrong choice! Do you wish to continue? [Y/N] ')).upper()[0]
        if cont in 'Nn':
            break
    print(f'\n Total of books register: {len(library)}.')

    a_file = open("lib_data.txt", "wb")
    pickle.dump(library,a_file)
    a_file.close()
    a_file = open("lib_data.txt", "rb")
    output = pickle.load(a_file)
    print(output)
    a_file.close()




#sorting list of dicts
# new_list = sorted(library, key = lambda i: i['name'])
# print(new_list)