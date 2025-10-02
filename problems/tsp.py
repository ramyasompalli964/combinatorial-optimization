import csv

def load_tsp_data(filename):
    tsp_data = []
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                if len(row) < 3: continue
                tsp_data.append((row[0], float(row[1]), float(row[2])))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return tsp_data

