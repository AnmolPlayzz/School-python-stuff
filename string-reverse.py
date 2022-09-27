a=input("Enter string -> ")
p=""
for i in range(len(a)-1,-1,-1):
    p+=a[i]
print("Reversed ->", p)