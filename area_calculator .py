print("**** AREA CALCULATOR ****")
print (""" SELECT 1 to get area of square
         SELECT 2 to get area of triangle
         SELECT 3 to get area of circle 
         SELECT 4 to get area of rectangle
         SELECT 5 to get area of ellipse
         SELECT 6 to get area of trapezoid
         SELECT 7 to get area of parallelogram """)

choice = int(input("Enter a number between 1 and 7: "))
if choice == 1:
    side = float(input("Enter lenght of a side: "))
    area = side * side
    print ("The area of the square is ", area)
elif choice == 2:
    base = float(input("Enter lenght of a base: "))
    height = float(input("Enter lenght of a height: "))
    area = 0.5 * base * height
    print ("The area of the triangle is ", area)
elif choice == 3:
    radius = float(input("Enter lenght of a radius: "))
    area = 3.14 * radius * radius
    print ("The area of the circle is ", area)
elif choice == 4:
    length = float(input("Enter lenght of a length: "))
    width = float(input("Enter lenght of a width: "))
    area = length * width
    print ("The area of the rectangle is ", area)
elif choice == 5:
    major_axis = float(input("Enter lenght of a major axis: "))
    minor_axis = float(input("Enter lenght of a minor axis: "))
    area = 3.14 * major_axis * minor_axis
    print ("The area of the ellipse is ", area)
elif choice == 6:
    side = float(input("Enter lenght of a side: "))
    height = float(input("Enter lenght of a height: "))
    area =(side * side) / 2 * height
    print ("The area of the trapezoid is ", area)
elif choice == 7:
     base = float(input("Enter lenght of a base: "))
     height = float(input("Enter lenght of a height: "))
     area = base * height
     print ("The area of the parallelogram is ", area)
