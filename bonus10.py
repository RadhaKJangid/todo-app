try:
    width = float(input("Enter width of the rectangle:"))
    length = float(input("Enter length of the rectangle:"))
    if width == length:
        exit("That looks like a square")

    area = length * width
    print(area)
except ValueError:
    print("Invalid input")