import csv

def load_knapsack_data(filename):
    knapsack_data = []
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                if len(row) < 3: continue
                knapsack_data.append((row[0], int(float(row[1])), int(float(row[2]))))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return knapsack_data

