l=[1,2,3,3,2,4,5,6,1,2,3]
a=l
dup=[]
org=[]
for i in l:
    if l.count(i)>1:
        if i not in dup:
            dup.append(i)
    else:
        org.append(i)
print(org)
print(dup)