import csv
with open(r'E:/pythonProject/file/123.csv') as file:
    data = csv.DictReader(file, delimiter=',', quotechar='"')
    for row in data:
        print(row['first_name'],row['last_name'])