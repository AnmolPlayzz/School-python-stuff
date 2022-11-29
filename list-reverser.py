#So basically, we have to reverse a list but without using an empty list, any finction (not even .pop) and slicing 
l=[1,2,3,4,5,6,7]
m=len(l)
for i in range((m+1)//2):
    a=l[m-1-i]
    b=l[i]
    l[m-1-i]=b
    l[i]=a
print(l)