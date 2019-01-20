import csv

data =[
    {"first_name":"Jose", "last_name":"JM"},
    {"first_name":"Pan", "last_name":"Twardowski"},
    {"first_name":"BSSS", "last_name":"HBS"},
    {"first_name":"Mark", "last_name":"Watney"}
]
with open(r'E:/pythonProject/file/123.csv', mode='w') as file:
    writer =csv.DictWriter(
        f=file,
        fieldnames=['first_name', 'last_name'],
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n')

    writer.writeheader()
    for row in data:
        writer.writerow(row)