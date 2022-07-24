import math

print("Select a shape from the following:\n\n1. Square\n2. Rectangle\n3. Circle\n4. Triangle\n5. Rhombus\n6. Trapezium\n7. Exit\n")
shape=input("Enter shape (list number, eg. 1 stands for square): ")

if shape=="1":
    square_side=eval(input("Enter side of square: "))
    print("Area of square:",square_side*square_side)
elif shape=="2":
    rectangle_length=eval(input("Enter length of rectangle: "))
    rectangle_width=eval(input("Enter width of rectangle: "))
    print("Area of rectangle:",rectangle_length*rectangle_width)
elif shape=="3":
    circle_radius=eval(input("Enter radius of circle: "))
    print("Area of circle:",3.14*circle_radius*circle_radius)
elif shape=="4":
    triangle_side_1=eval(input("Enter side 1 of triangle: "))
    triangle_side_2=eval(input("Enter side 2 of triangle: "))
    triangle_side_3=eval(input("Enter side 3 of triangle: "))
    semiperimeter=(triangle_side_1+triangle_side_2+triangle_side_3)/2
    area=math.sqrt((semiperimeter*(semiperimeter-triangle_side_1)*(semiperimeter-triangle_side_2)*(semiperimeter-triangle_side_3)))
    print("Area of triangle:",area)
elif shape=="5":
    rhombus_diagonal_1=eval(input("Enter diagonal 1 of rhombus: "))
    rhombus_diagonal_2=eval(input("Enter diagonal 2 of rhombus: "))
    print("Area of rhombus:",(rhombus_diagonal_1*rhombus_diagonal_2)/2)
elif shape=="6":
    trapezium_base_1=eval(input("Enter base 1 of trapezium: "))
    trapezium_base_2=eval(input("Enter base 2 of trapezium: "))
    trapezium_height=eval(input("Enter height of trapezium: "))
    print("Area of trapezium:",(trapezium_base_1+trapezium_base_2)*trapezium_height/2)
elif shape=="7":
    print("Exiting...")
    exit()
else:
    print("Invalid input")
    print("Exiting...")
    exit()