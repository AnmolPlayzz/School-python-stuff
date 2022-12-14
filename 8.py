l=eval(input("Enter list -> "))
c=0
n=int(input("Enter number to search -> "))
for i in l:
    if i==n:
        c+=1
print(n, "occours", c, "times in", l)