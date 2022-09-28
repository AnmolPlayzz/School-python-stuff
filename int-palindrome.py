n=int(input("Enter number -> "))
p=0
c=n
while c!=0:
    a=c%10
    p=(p*10)+a
    c=c//10
if p==n:
    print("palindrome")
else:
    print("not palindrome")