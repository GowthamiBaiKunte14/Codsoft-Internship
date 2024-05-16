#define operations

def addition(n1,n2):
    return n1 + n2
def subraction(n1,n2):
    return n1 - n2
def multiplication(n1,n2):
    return n1 * n2
def division (n1,n2):
    return n1 / n2

print("Select an operation to perform:")
print("1. Addition\n")
print("2. Subtraction\n")
print("3. Multiplication\n")
print("4. Division")

operation = int(input("Enter choice of operation 1/2/3/4: "))

#Taking inputs

n1 = float(input("Enter the First Number: "))
n2 = float(input("Enter the Second Number: "))

#Applying conditions

if operation == 1:
    print(n1, "+",n2,"=", addition(n1,n2))  
elif operation == 2:
    print(n1, "-",n2,"=", subtraction(n1,n2))  
elif operation == 3:
    print(n1, "*",n2,"=", multiplication(n1,n2))  
elif operation ==  4:
    print(n1, "/",n2,"=", division(n1,n2))  
else:
    print("Invalid Entry")


