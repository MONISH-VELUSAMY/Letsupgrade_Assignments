#to find the list of persons from whom they have received their gifts
donor=[2,1,5,3,4]
rvr={}
count=1
for i in donor:
   if i==1:
      rvr[i]=count
      break
   else:
      count=count+1

count=1
for i in donor:
   if i==2:
      rvr[i]=count
      break
   else:
      count=count+1
     
count=1
for i in donor:
   if i==3:
      rvr[i]=count
      break
   else:
      count=count+1
  


count=1
for i in donor:
   if i==4:
      rvr[i]=count
      break
   else:
      count=count+1

count=1
for i in donor:
   if i==5:
      rvr[i]=count
      break
   else:
      count=count+1
#print(rvr)
print("gift_receiver:",list(rvr.values()))
