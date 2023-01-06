s=input("Enter string -> ")
n=""
for i in range(0,len(s)):
    if i%2==0:
        n+=s[i].upper()
    else:
        n+=s[i].lower()
print(n)