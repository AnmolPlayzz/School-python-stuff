s=input("Enter string -> ")
l=s.split(" ")
j=0
for i in range(1,len(l)):
    if len(l[i])>len(l[j]):
        j=i
print("Longest sub-string -> ", l[j])
