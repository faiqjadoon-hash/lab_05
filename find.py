import argparse

parser = argparse.ArgumentParser()
parser.add_argument("pattern")
parser.add_argument("filename")
parser.add_argument("-i", "--ignore-case", action="store_true")

args = parser.parse_args()

with open(args.filename) as file:
    for line_number, line in enumerate(file, start=1):
        text = line.rstrip("\n")

        if args.ignore_case:
            if args.pattern.lower() in text.lower():
                print(f"{line_number}: {text}")
        else:
            if args.pattern in text:
                print(f"{line_number}: {text}")