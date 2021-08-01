#to convert temperature using formulae
choice=int(input("enter 1 for celsius to fahrenheit or 2 for fahrenheit to celsius:"))
if(choice == 1):
    cel=float(input("enter the temperature in celsius:"))
    far=(cel*1.8)+32
    print("Fahrenheit = {:.2f}".format(far))
elif(choice==2):
    far=float(input("enter the temperature in fahrenheit:"))
    cel=(far-32)*5/9
    print("Celsius = {:.2f}".format(cel))
else:
   print("please enter 1 or 2.Try again.")
