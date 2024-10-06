def main():
    path = "books/frankenstein.txt"
    bookcontnet = readbook(path)
    countofwords = countWords(bookcontnet)
    dicofchar = countChar(bookcontnet)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{countofwords} words foudn in the documnet\n')
    printreport(dicofchar)
    print("--- End report ---")

def readbook(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def countWords(bookcontent):
    newarray = bookcontent.split()
    #print(newarray)
    count =0
    for string in newarray:
        count +=1
    return count

def countChar(bookcontnet):
    newsting = bookcontnet.lower()
    #print(newsting)
    newdict = {}
    for char in newsting:
        #print(char)
        if char in newdict:
            newdict[char] +=1
        else:
            newdict[char] = 1
    return newdict

def printreport(dicofchar):
    words = "asdfghjklzxcvbnmqwertyuiop"
    for item in dicofchar:
        if item in words:
            print(f'{item} character was found {dicofchar[item]} times')

main()