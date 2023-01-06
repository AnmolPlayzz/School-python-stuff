s1=input("First string -> ")
s2=input("Second string -> ")
s=s2[:-1]+s1[-1]+" "+s1[:-1]+s2[-1]
print(s)