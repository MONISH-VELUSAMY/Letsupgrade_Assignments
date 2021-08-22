#to create 6 character OTP


import string
import random as rand
char_list=list(string.ascii_letters+string.digits)
otp=''
for i in range(6):
   otp+=rand.choice(char_list)
print("OTP:",otp)
