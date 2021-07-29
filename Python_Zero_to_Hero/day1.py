list=[]
n=int(input("enter the n:"))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print("the original list:")
print(list)

x=sorted(list,reverse=True)
print("the descending order:")
print(x)
