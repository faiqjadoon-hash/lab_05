import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("column")
parser.add_argument("value")

args = parser.parse_args()

with open(args.filename, newline="") as file:
    reader = csv.reader(file)
    rows = list(reader)

header = rows[0]
column_index = header.index(args.column)

for row in rows[1:]:
    if row[column_index] == args.value:
        print(",".join(row))