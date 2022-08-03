#pretend like a**b does not exist 👍
n=int(input("Enter a number: "))
e=int(input("Enter a power: "))
ans=1
for i in range(1,e+1):
    ans*=n
print("Result is",ans)