# to make a calculator 

def sum(a, b):
    return float(a+b)

def sub(a, b):
    return float(a-b)

def mul(a, b):
    return float(a*b)

def div(a, b):
    return float(a/b)

def power(a, b):
    return float(a**b)

def modulo(a, b):
    return a%b

def modulus(a):
    if a>=0:
        return a
    else:
        return (-a)
    
func = input("Enter the operation that you want to execute: ")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if func == "sum":
    print(sum(a, b))
elif func == 'subraction':
    print(sub(a, b))
elif func == 'multiplication':
    print(mul(a, b))
elif func =='division':
    print(div(a, b))
elif func == 'power':
    print(power(a, b))
elif func == 'modulo':
    print(modulo(a, b))
elif func == 'modulus':
    x = input("You want modulus value for which number?")
    if x == a:
        print(modulus(a))
    elif x == b:
        print(modulus(b))
    else:
        print("Invalid value entered.")
else:
    print("Function not found in the calculator. Sorry.")
    