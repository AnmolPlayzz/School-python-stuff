n=int(input("Enter the number of terms: "))
a=0
b=1
i=1
while i<=n:
    c=a+b
    print(c)
    a=b
    b=c
    i+=1