def tsp_dp(tsp_data):
    return tsp_data  # placeholder

def knapsack_dp(knapsack_data, capacity=50):
    n = len(knapsack_data)
    if n == 0: return []
    capacity = int(capacity)
    dp = [[0]*(capacity+1) for _ in range(n+1)]
    for i in range(1,n+1):
        item, weight, value = knapsack_data[i-1]
        for w in range(capacity+1):
            if weight <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight]+value)
            else:
                dp[i][w] = dp[i-1][w]
    # Backtrack
    w = capacity
    selected = []
    for i in range(n,0,-1):
        if dp[i][w] != dp[i-1][w]:
            item, weight, value = knapsack_data[i-1]
            selected.append(knapsack_data[i-1])
            w -= weight
    return selected[::-1]

