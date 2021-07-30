#To generate One Time Password using letters and digits
import random as r
import string
len=6
chars=string.ascii_letters + string.digits
otp=''
for i in range(len):
  otp=otp+r.choice(chars)
print("otp:",otp)
