import re
import csv
import sys


def parse_line(line):
    # gets the name and dob from each line
    line = line.strip()

    match = re.match(r"^(.*?)\s+(\d{2}/\d{2}/\d{4})$", line)

    if match:
        name = match.group(1).strip()
        dob = match.group(2).strip()
        return name, dob

    return None, None


def read_file(filename):
    # read the text file and split good and bad lines
    entries = []
    bad_lines = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if line.strip():
                    name, dob = parse_line(line)

                    if name and dob:
                        entries.append((name, dob))
                    else:
                        bad_lines.append((line_number, line.strip()))

    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
        sys.exit()

    return entries, bad_lines


def print_results(entries):
    print("\nNames")
    for name, dob in entries:
        print(name)

    print("\nDates of Birth")
    for name, dob in entries:
        print(dob)


def save_to_csv(entries, filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Date of Birth"])
        writer.writerows(entries)

    print(f"\nSaved CSV to {filename}")


def save_to_txt(entries, bad_lines, filename):
    with open(filename, "w", encoding="utf-8") as file:

        file.write("Names\n")
        for name, dob in entries:
            file.write(name + "\n")

        file.write("\nDates of Birth\n")
        for name, dob in entries:
            file.write(dob + "\n")

        if bad_lines:
            file.write("\nInvalid lines\n")
            for line_number, line in bad_lines:
                file.write(f"Line {line_number}: {line}\n")

    print(f"Saved TXT report to {filename}")


def print_bad_lines(bad_lines):
    if bad_lines:
        print("\nInvalid lines found:")
        for line_number, line in bad_lines:
            print(f"Line {line_number}: {line}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python parser.py input.txt output.csv")
        sys.exit()

    input_file = sys.argv[1]
    output_csv = sys.argv[2]
    output_txt = "report.txt"

    print(f"Reading file: {input_file}")

    entries, bad_lines = read_file(input_file)

    if entries:
        print_results(entries)
        save_to_csv(entries, output_csv)
        save_to_txt(entries, bad_lines, output_txt)
    else:
        print("No valid records found.")

    print_bad_lines(bad_lines)


if __name__ == "__main__":
    main()