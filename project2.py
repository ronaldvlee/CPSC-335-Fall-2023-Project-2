from typing import List

# M is the budget, int
#
# items is the List of stocks, contains
#   [𝑥,𝑦] attributes, where 
#       𝑥 = numbers of trading stocks and 
#       𝑦 = monetary value of the trading stocks

def stock_maximization_exhaustive(M: int, items: List[List[int]]) -> int:
    # Define a recursive function to exhaustively maximize profit
    def maximize(index: int, remaining_M: int):
        # Base case: if the index is out of bounds or no more budget remaining
        if index < 0 or remaining_M <= 0:
            return 0, set()  # Return zero profit and an empty set of selected stocks

        # Initialize variables to track included stocks and their quantities
        number_of_included_stocks, included_stocks = 0, set()
        
        # Extract quantity and value of the current stock
        quantity, value = items[index]

        # Check if the current stock can be included within the remaining budget
        if remaining_M >= value:
            # Recursively call the function for the case where the current stock is included
            number_of_included_stocks, included_stocks = maximize(index - 1, remaining_M - value)
            
            # Update the number of included stocks and add the current stock to the set
            number_of_included_stocks += quantity
            included_stocks.add((quantity, value))

        # Recursively call the function for the case where the current stock is excluded
        number_of_excluded_stocks, excluded_stocks = maximize(index - 1, remaining_M)

        # Compare the results and return the configuration with the higher profit
        if number_of_included_stocks >= number_of_excluded_stocks:
            return number_of_included_stocks, included_stocks
        else:
            return number_of_excluded_stocks, excluded_stocks

    # Start the recursive maximization from the last item and the given budget
    return maximize(len(items) - 1, M)

def stock_maximization_dynamic(M: int, items: List[List[int]]) -> int:
    # Get the number of items
    n = len(items)

    # Create a 2D array (dp) to store intermediate results for dynamic programming
    # dp[i][j] represents the maximum profit using the first i items and a maximum budget of j
    dp = [[0] * (M + 1) for _ in range(n + 1)]

    # Iterate through each item
    for i in range(1, n + 1):
        stock_count, stock_value = items[i - 1]

        # Iterate through each possible budget (j)
        for j in range(M + 1):
            # Check if the current item's value is less than or equal to the current budget
            if stock_value <= j:
                # If it is, choose the maximum between excluding the current item and including it
                dp[i][j] = max(dp[i - 1][j], 
                               dp[i - 1][j - stock_value] + stock_count)
            else:
                # If the current item's value is greater than the budget, exclude the item
                dp[i][j] = dp[i - 1][j]

    # The final result is stored in the bottom-right cell of the dp array
    max_stocks = dp[n][M]

    # Track the selected stocks using a set
    selected_stocks = set()

    # Backtracking the selected stocks from the dp array to show selected
    i, j = n, M
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            stock_count, stock_value = items[i - 1]
            selected_stocks.add((stock_count, stock_value))
            j -= stock_value
        i -= 1

    # Return the maximum profit and the set of selected stocks
    return max_stocks, selected_stocks