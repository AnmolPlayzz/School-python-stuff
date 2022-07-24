a=eval(input("Enter first number: "))
b=eval(input("Enter second number: "))
print("\n\nSelect an operation:\n1. +\n2. -\n3. *\n4. /\n5. %\n6. **\n7. //\n8. exit")
operator=input("Enter operator: ")
if type(a)==int and type(b)==int:
    if operator=="+":
        print(a+b)
    elif operator=="-":
        print(a-b)
    elif operator=="*":
        print(a*b)
    elif operator=="/":
        print(a/b)
    elif operator=="%":
        print(a%b)
    elif operator=="**":
        print(a**b)
    elif operator=="//":
        print(a//b)
    elif operator=="exit":
        print("Exiting...")
        exit()
    else:
        print("Invalid operator")
        print("Exiting...")
        exit()
else:
    print("Invalid input")
    print("Exiting...")
    exit()