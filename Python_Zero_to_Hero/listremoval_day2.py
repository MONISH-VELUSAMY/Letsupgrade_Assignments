#To remove all the occurences of a specific item in the list
list=[1, 3, 1, 1, 1, 1]
num=int(input("enter the number to delete:"))
l=[i for i in list if i!=num]
print(l)
