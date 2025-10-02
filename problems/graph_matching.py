import csv

def load_graph_data(filename):
    graph_data = []
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                if len(row) < 3: continue
                graph_data.append((row[0], row[1], float(row[2])))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return graph_data


