l=eval(input("Enter list -> "))
maxm=0
for i in l:
    if l>maxm:
        maxm=l
minm=maxm
for j in l:
    if l<minm:
        minm=l
print("Maximum ->", maxm)
print("Minimum ->", minm)