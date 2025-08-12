print ("Hello and welcome to the Task 2 calculator!")
#Defining inital calculator inputs
operator, num1, num2 = input("Please input your operator and 2 numbers: ").split()
if operator not in ['+', '-', 'x', '/']:
   print("invalid operation.")
   exit
if operator == "+":
   print(int(num1) + int(num2)) 
elif operator == "*":
   print(int(num1) * int(num2)) 
elif operator == "/":
   print(int(num1) / int(num2)) 
elif operator == "-":
   print(int(num1) - int(num2)) 
elif