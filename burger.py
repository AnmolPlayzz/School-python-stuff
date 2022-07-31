print("Welcome to MCDonalds")
print("\n\nMenu:\n1. Burgers\n2. Ice Cream\n3. Fries")
option=int(input("Select an input.\n\nUse numbers to specify (eg. 1 stands for Burger)\n\n->"))
cost=0

if option==1:
    print("Welcome to the Burger creation menu\n")
    burger_tikki=int(input("\nEnter no. of tikki (Cost of 1 tikki = Rs. 30)\n\n-> "))
    cost=cost+burger_tikki*30
    print("Noted, we'll add", burger_tikki, "tikkis!")

    burger_m=input("Add mayonnese (Rs. 5)\nReply with \"yes\" or \"no\"\n\n-> ")
    if burger_m=="yes":
        cost=cost+5
        print("Added!")
    else:
        print("Ok!")

    burger_c=input("Add cheese (Rs. 10)\nReply with \"yes\" or \"no\"\n\n-> ")
    if burger_c=="yes":
        cost=cost+10
        print("Added!")
    else:
        print("Ok!")
    
    burger_s=input("Add sauce (Rs. 5)\nReply with \"yes\" or \"no\"\n\n-> ")
    if burger_s=="yes":
        cost=cost+5
        print("Added!")
    else:
        print("Ok!")

if option==2:
    print("Welcome to the Ice Cream creation menu\n")
    ice_cream=int(input("\nEnter no. of scoops (Cost of 1 scoop = Rs. 20)\n\n-> "))
    cost=cost+ice_cream*20
    print("Noted, we'll add", ice_cream, "scoops!")

    ice_cream_c=input("Add chocolate toppings (Rs. 10)\nReply with \"yes\" or \"no\"\n\n-> ")
    if ice_cream_c=="yes":
        cost=cost+10
        print("Added!")
    else:
        print("Ok!")

    ice_cream_s=input("Add sprinkles (Rs. 5)\nReply with \"yes\" or \"no\"\n\n-> ")
    if ice_cream_s=="yes":
        cost=cost+5
        print("Added!")
    else:
        print("Ok!")

if option==3:
    print("Welcome to the Fries creation menu\n")
    fries=int(input("\nEnter no. of fries (Cost of 1 fries = Rs. 10)\n\n-> "))
    cost=cost+fries*10
    print("Noted, we'll add", fries, "fries!")

    fries_c=input("Add cheese (Rs. 10)\nReply with \"yes\" or \"no\"\n\n-> ")
    if fries_c=="yes":
        cost=cost+10
        print("Added!")
    else:
        print("Ok!")

    fries_s=input("Add sauce (Rs. 5)\nReply with \"yes\" or \"no\"\n\n-> ")
    if fries_s=="yes":
        cost=cost+5
        print("Added!")
    else:
        print("Ok!")

print("Your total cost is Rs.", cost)