#PROGRAM, REMOVE ALL '*' WITHOUT USING A REPLACE FUNCTION
#join() convert the list to string
def fun1(st):
    #creat a list for storing a element of string
    newList=[]
    for j in st:
        if j != '*':
            newList.append(j)
            continue
    return (''.join(newList))
s=input("enter a given string:")
print("string after removing '*' : %s"%fun1(s))
