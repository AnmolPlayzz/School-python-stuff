n=int(input("Enter number -> "))
s=0
c=n
while c!=0:
    s=s+(c%10)
    c=c//10
print("Sum = ", s)