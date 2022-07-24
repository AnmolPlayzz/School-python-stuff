maths=eval(input("Enter marks in maths: "))
physics=eval(input("Enter marks in physics: "))
chemistry=eval(input("Enter marks in chemistry: "))
english=eval(input("Enter marks in english: "))
computer=eval(input("Enter marks in computer science: "))

total=maths+physics+chemistry+english+computer
percentage=total*100/500
grade=None
if percentage>=90:
    grade="A"
elif percentage>=85 and percentage<90:
    grade="B"
elif percentage>=80 and percentage<85:
    grade="C"
else:
    grade="D"

print("Total marks: ",total)
print("Percentage: ",total*100/500)
print("Grade: ",grade)