def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def modulus(x,y):
    if y == 0:
        return "Division by zero is not allowed"
    else:
        return x / y
def division(x,y):
    return x/y

x=float(input("Enter your first number \n"))
print('1. Add')
print('2. Subtraction')
print('3. Multiplication')
print('4. Modulus')
print('5. Division')
sign=int(input("Select your operation of choice 1,2,3,4,5 \n"))
y=float(input("Enter your second number\n"))

if sign==1:
    print (add(x,y))
elif sign==2:
    print (subtract(x,y))
elif sign==3:
    print (multiply(x,y)) 
elif sign==4:
      print (modulus(x,y))
elif sign==5:
    print (division(x,y))              
else:
    print("INVALID SIGN")

