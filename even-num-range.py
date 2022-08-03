n=int(input("Enter a number: "))
a=0
for i in range(0,n+1,2):
    a=a+i
print("The sum of the even numbers from 1 to",n,"is",a)