l={}
n=int(input("Enter no. of terms to add -> "))
for i in range(n):
    h=eval(input("Enter key -> "))
    k=eval(input("Enter value -> "))
    l.update({h:k})
print(l)