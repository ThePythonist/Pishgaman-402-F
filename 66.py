def checkword(word):
    if len(word) == len(set(word)):
        return "Tekrari nadarad"
    else:
        return "Tekrari darad"


word = input("Enter any word : ")
print(checkword(word))
