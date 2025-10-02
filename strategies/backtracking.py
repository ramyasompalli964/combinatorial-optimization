def knapsack_backtracking(knapsack_data, capacity=50):
    n = len(knapsack_data)
    best_value = 0
    best_solution = []
    def backtrack(i, current_value, current_weight, current_solution):
        nonlocal best_value, best_solution
        if i == n:
            if current_value > best_value:
                best_value = current_value
                best_solution = current_solution[:]
            return
        item, weight, value = knapsack_data[i]
        if current_weight + weight <= capacity:
            backtrack(i+1, current_value+value, current_weight+weight, current_solution+[knapsack_data[i]])
        backtrack(i+1, current_value, current_weight, current_solution)
    backtrack(0,0,0,[])
    return best_solution

