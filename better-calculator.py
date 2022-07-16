#Not officially done in school, but I did it in my free time.

print("Preffer entering larger number first\n")

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

print("\nSelect an operation from the following:\n\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n\n")

operator=input("Enter operator:")

if operator=="Add" or operator=="Subtract" or operator=="Multiply" or operator=="Divide":
    if operator=="Add":
        print("Sum:", a+b)

    if operator=="Subtract":
        print("Difference:", a-b)

    if operator=="Multiply":
        print("Product:", a*b)

    if operator=="Divide":
        print("Quotient:", a/b)

else:
    print("Invalid operator")