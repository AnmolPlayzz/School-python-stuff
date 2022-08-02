#a condensed version
#won't merge this one into main branch

a=input("Enter first number: ")
b=input("Enter second number: ")
print("\n\nSelect an operation:\n1. +\n2. -\n3. *\n4. /\n5. %\n6. **\n7. //")
op=input("Enter operator: ")
if type(a)==int and type(b)==int:
    if op=="+" or op=="-" or op=="*" or op=="/" or op=="%" or op=="**" or op=="//":
        out=eval(str(a)+op+str(b))
        print("Answer:", out)
    else:
        print("Invalid operator")
        print("Exiting...")
else:
    print("Invalid input")
    print("Exiting...")