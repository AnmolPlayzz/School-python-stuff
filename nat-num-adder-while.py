n=int(input("Enter the total number of numbers: "))
a=0
s=1
while s<=n:
    num=int(input("Enter a number: "))
    a=a+num
    s+=1
print("The sum of the numbers is",a)