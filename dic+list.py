d={}
n=int(input("Enter no. of entries -> "))
for i in range(n):
    na=input("Enter name -> ")
    for j in range(3):
        mh=int(input("Maths -> "))
        ph=int(input("Physics -> "))
        ch=int(input("Chemistry -> "))
        l=[mh,ph,ch]
        break
    d.update({na:l})
print(d)