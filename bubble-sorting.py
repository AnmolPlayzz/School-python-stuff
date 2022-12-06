l=[6,9,4,2,0]
for i in range(len(l)):
    for j in range(i-1,-1,-1):
        l[j],l[j+1]=l[j+1],l[j]
print(l)