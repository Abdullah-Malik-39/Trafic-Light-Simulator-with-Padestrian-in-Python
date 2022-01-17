var1 = int(input("Enter Age : "))
var2 = input("Enter sex(M/F) : ")
var3 = input("Enter Marital Status(Y/N) : ")
if var2 == "M":
   if 20 <= var1 <40 :
      print("Can work Anywhere")
   elif 40 <= var1 <60 : 
      print("Can work only in Urban Areas")
elif var2 == "F":
   print("Can work only in Urban Areas")
else:
   print("ERROR")
