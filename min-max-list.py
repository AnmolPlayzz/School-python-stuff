l=eval(input("Enter list -> "))
maxm=0
for i in l:
    if i>maxm:
        maxm=i
minm=maxm
for j in l:
    if j<minm:
        minm=j
print("Maximum ->", maxm)
print("Minimum ->", minm)