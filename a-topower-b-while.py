#pretend like a**b does not exist (again, don't get me wrong.. I like reinventing the wheel just like the next javascript developer - yes I am a native jser) 👍
n=int(input("Enter a number: "))
e=int(input("Enter a power: "))
ans=1
i=1
while i<=e:
    ans*=n
    i+=1
print("Result is",ans)