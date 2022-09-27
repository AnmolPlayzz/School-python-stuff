a=0
print("Use the calculator like a GUI one\nNumber -> Operator-> Number-> And so on")
print("\n--------------\n0")
while True:
    op=input()
    if op=="=":
        print(a)
        break
    else:
        n=int(input())
        if op=="+":
            a+=n
        elif op=="-":
            a-=n
        elif op=="*":
            a*=n
        elif op=="/":
            a=a/n
        else:
            print("Invalied operator")