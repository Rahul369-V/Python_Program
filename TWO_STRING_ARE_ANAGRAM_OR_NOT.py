#Anagram or Not

s=input("Enter a string: ") # input read everything as STRING!!!
y=input("Enter a string: ")
if(sorted(s)==sorted(y)):
    print("There are ANAGRAM!!!!!")
else:
    print("There are not ANAGRAM!!!!")
