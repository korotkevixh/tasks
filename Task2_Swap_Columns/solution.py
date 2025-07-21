import csv

def swap_columns():
    with open("stdin.csv", "r") as src, open("stdout.csv", "w", newline = "") as dst:
        reader = list(csv.reader(src))
        transposed = list(zip(*reader))
        reordered = [transposed[0], transposed[2], transposed[1]]
        rows = zip(*reordered)
        writer = csv.writer(dst)
        for row in rows:
            writer.writerow(row)

def main():
    swap_columns()

if __name__ == "__main__":
    main()