from converters import convert
from parsers import parse

feet_inches = input("Enter feet and inches: ")

f, i = parse(feet_inches)
print("fi", f, i)
result = convert(f, i)

if result < 1:
    print("Kid is too small")
elif result > 1:
    print("Kid can use the slide.")
