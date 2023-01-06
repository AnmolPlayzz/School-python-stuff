s=input("Enter string -> ")
l=""
for i in range(len(s)-1,-1,-1):
    l+=s[i]
if s==l:
    print("Palindrome")
else:
    print("Not palindrome")