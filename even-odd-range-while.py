n=int(input("Enter number -> "))
a=1
e=0
o=0
while a<=n:
    if a%2!=0:
        o+=a
    else:
        e+=a
    a+=1
print("Sum of odd numbers:",o,"\nSun of even number:",e)