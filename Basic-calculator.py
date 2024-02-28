def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
      
      return "Cannot divide by zero"
    else:
        return x/y
def mod(x,y):
    if y==0:
     return "Cannot divide by zero"
    else:
      return x%y
print("select operation")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("5.mode")

while True:
    choice=input("enter choice(1/2/3/4/5):")
    if choice in ('1','2','3','4','5'):
        num1=float(input('Enter first number:'))
        num2=float(input("Enter second number:"))
        if choice =='1':
           print("Result:",add(num1,num2))
        elif choice=='2':
           print("Result:",sub(num1,num2))
        elif choice=='3':
           print("Result:",mul(num1,num2))
        elif choice=='4':
           print("Result:",div(num1,num2))
        elif choice=='5':
           print("Result:",mod(num1,num2))
        break
    else:
       print("Invalid Input")
  

