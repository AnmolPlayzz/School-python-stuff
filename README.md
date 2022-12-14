# All term 2 programmes
(at least the ones I have)

---

- Lists
    1. Add items to list
        ```py
        l=[]
        n=int(input("Enter no. -> "))
        for i in range(n):
            l.append(int(input("-> ")))
        ```
    2. Check if element exists in list
        ```py
        l=[]
        n=int(input("Enter no. -> "))
        for i in range(n):
            l.append(int(input("-> ")))
        m=int(input("Enter number to search -> "))
        for j in range(len(l)):
            if l[j]==m:
                print(m,"is found.")
                break
            else:
                continue
        ```
    3.  Find minimum and maximum no. in a list
        ```py
        l=eval(input("Enter list -> "))
        maxm=0
        for i in l:
            if i>maxm:
                maxm=i
        minm=maxm
        for j in l:
            if j<minm:
                minm=j
        print("Maximum ->", maxm)
        print("Minimum ->", minm)
        ```
    4. List reverse using a new list
        ```py
        l=[1,2,3,4,5,6,7]
        n=[]
        for i in range(len(l)-1,-1,-1):
            n.append(l[i])
        print(n)
        ```
    5. List reverse without a new list/functions
        ```py
        l=[1,2,3,4,5,6,7]
        m=len(l)
        for i in range((m+1)//2):
            a=l[m-1-i]
            b=l[i]
            l[m-1-i]=b
            l[i]=a
        print(l)
        ```
    6. Bubble sorting
        ```py
        l=[6,9,4,2,0]
        for i in range(len(l)):
            for j in range(i-1,-1,-1):
                if l[j+1]<l[j]:
                    l[j],l[j+1]=l[j+1],l[j]
        print(l)
        ```
    7. Count elements in a list
        ```py
        l=eval(input("Enter list -> "))
        n=int(input("Enter number -> "))
        c=0
        for i in l:
            if n==i:
                c+=1
        print(n,"occours",c,"times in",l)
        ```
- Dictionary 
    1. Update a dictionary
        ```py
        l={,}
        n=int(input("Enter no. of terms to add -> "))
        for i in range(n):
            h=eval(input("Enter key -> "))
            k=eval(input("Enter value -> "))
            l.update({h:k})
        print(l)
        ```
    2. collect marks in a list and add them to a list and add it to a dictionary
        ```py
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
        ```
- Modules
    1. Math
        ```py
        import math
        print(math.sqrt(81))
        print(math.ceil(6.9))
        print(math.floor(5.9))
        print(math.e)
        print(math.pi)
        print(math.sin(math.pi/6))
        print(math.fabs(-69.420))
        print(math.fabs(-5))
        ```


Well, that's all I had.
