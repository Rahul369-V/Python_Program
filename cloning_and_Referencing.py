# cloning/copying
print("\nthis is referencing..")
b = [1, 2, 3]
print("main list :",b)
m = b  # this is referencing ,this is not cloning

print("M list  referencing:",m)
print("id of referenced m list:", id(m)) # ID ARE  SAME FOR THE TWO LIST BECAUSE IT IS referencing
print("id of main list:", id(b),"\n")

print("this is cloning or copying...")
# copying n list to m list
m = b[:]
print("copied M LIST :",m)
print("id of copied m list:",id(m))
print("id of main list:",id(b))

a = list(b)  # this also copying only
print(a)
