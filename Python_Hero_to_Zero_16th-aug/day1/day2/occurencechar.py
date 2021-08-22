#to count the occurences of each char in the given string
str=input("enter the string:")
dict={}
for ele in str:
  if ele in dict:
         dict[ele]+=1
  else:
          dict[ele]=1
print(dict)
       
