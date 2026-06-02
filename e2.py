import csv


with open("data.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter your city: ")

for row in data:
    if row[0] == city:
        print(row[1])