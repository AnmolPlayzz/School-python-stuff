maths=eval(input("Enter marks in maths: "))
physics=eval(input("Enter marks in physics: "))
chemistry=eval(input("Enter marks in chemistry: "))
english=eval(input("Enter marks in english: "))
computer=eval(input("Enter marks in computer science: "))

total=maths+physics+chemistry+english+computer

print("Total marks: ",total)
print("Percentage: ",total*100/500)