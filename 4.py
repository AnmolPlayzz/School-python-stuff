l=[1,2,3,4,5,6,7,8,9]
for i in range((len(l)+1)//2):
    l[len(l)-1-i],l[i]=l[i],l[len(l)-1-i]
print(l)