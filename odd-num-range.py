n=int(input("Enter a number: "))
a=0
for i in range(1,n+1,2):
    a=a+i
print("The sum of the odd numbers from 1 to",n,"is",a)