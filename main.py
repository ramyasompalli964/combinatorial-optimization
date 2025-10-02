# main.py

from problems.tsp import load_tsp_data
from problems.knapsack import load_knapsack_data
from problems.graph_matching import load_graph_data

from strategies.greedy import tsp_greedy, knapsack_greedy
from strategies.dynamic_programming import tsp_dp, knapsack_dp
from strategies.backtracking import knapsack_backtracking

from utils.performance import measure_time

# ======================
# Load datasets
# ======================

tsp_file = 'datasets/tsp_data.csv'
knapsack_file = 'datasets/knapsack_data.csv'
graph_file = 'datasets/graph_data.csv'

tsp_data = load_tsp_data(tsp_file)
knapsack_data = load_knapsack_data(knapsack_file)
graph_data = load_graph_data(graph_file)

# ======================
# TSP Algorithms
# ======================

print("\n--- TSP Greedy ---")
tsp_greedy_result = measure_time(tsp_greedy, tsp_data)
print(tsp_greedy_result)

print("\n--- TSP DP ---")
tsp_dp_result = measure_time(tsp_dp, tsp_data)
print(tsp_dp_result)

# ======================
# Knapsack Algorithms
# ======================

print("\n--- Knapsack Greedy ---")
knapsack_greedy_result = measure_time(knapsack_greedy, knapsack_data, 50)
print(knapsack_greedy_result)

print("\n--- Knapsack DP ---")
knapsack_dp_result = measure_time(knapsack_dp, knapsack_data, 50)
print(knapsack_dp_result)

print("\n--- Knapsack Backtracking ---")
knapsack_bt_result = measure_time(knapsack_backtracking, knapsack_data, 50)
print(knapsack_bt_result)

# ======================
# Graph Matching (placeholder)
# ======================

print("\n--- Graph Matching Data ---")
print(graph_data)
