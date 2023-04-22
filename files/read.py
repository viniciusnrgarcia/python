from concurrent.futures import ThreadPoolExecutor
import os
import csv

project_dir = os.path.dirname(__file__)
input_file_name = 'input.csv'
input_file = os.path.join(project_dir, input_file_name)
output_file_name = 'output.csv'
output_file = os.path.join(project_dir, output_file_name)

list = []
with open(input_file, 'r',) as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        id = row['id']
        product = row['product']
        price = row['price']
        print(id, product, price)
        list.append(row)

    csv_file.close()

print(list)

for i in list:
    print(i)



def f1(item):
    print(item)

# Concurrency
with ThreadPoolExecutor(max_workers=1) as executor:
    executor.map(f1, enumerate(list))
    executor.shutdown()