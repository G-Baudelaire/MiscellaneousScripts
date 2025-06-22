import csv
import sys


def clean(pair):
    return pair[0].strip(), pair[1].strip()


def make_pairs(lines):
    # Remove Lines Not Containing '='
    equality_lines = list(line for line in lines if "=" in line)
    # Make pairs from equalities and remove whitespace
    pairs = list(map(lambda pair_line: clean(pair_line.split('=')), equality_lines))
    return pairs


def read_raw_file(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError

    lines = read_raw_file(sys.argv[1])
    pairs = make_pairs(lines)

    write_file = rf'anki_words/lesson_{sys.argv[2]}.csv'
    with open(write_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(pairs)
        print(f"Successfully wrote {len(pairs)} pairs to {write_file}.")
