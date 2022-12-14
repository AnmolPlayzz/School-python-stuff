l=[]
n=int(input("Enter no. -> "))
for i in range(n):
    l.append(int(input("-> ")))
m=int(input("Enter number to search -> "))
s=str(m)+" is found"
for j in range(len(l)):
    if l[j]==m:
        s=str(m)+" is found"
        break
    else:
        s=str(m)+" isn\'t found"
print(s)