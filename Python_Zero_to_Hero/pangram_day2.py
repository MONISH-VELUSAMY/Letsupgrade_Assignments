#To check whether a sentence is pangram or not
import string
str=input("enter the string:")
chars=string.ascii_lowercase

flag=0
for i in chars:
    if i not in str.lower():
            flag=1
            break
            
if flag==0:
     print("yes it is pangram")
else:
     print("no it is not pangram")

