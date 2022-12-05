import csv
import time
import os
import json

project_dir = os.path.dirname(__file__)
input_file_name = 'input.csv'
input_file = os.path.join(project_dir, input_file_name)
output_file_name = 'output.json'
output_file = os.path.join(project_dir, output_file_name)

def generate_output(array):
    try:
        with open(output_file, 'w',) as jsonFile:
            jsonFile.write(json.dumps(array, indent=4))
    except Exception as e:
        print(e, e.__cause__, e.__class__)


took = time.perf_counter()

items = []
data = {}
with open(input_file, 'r', ) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for row in csvReader:
        items.append(row)
        data = row


generate_output(array=items)


