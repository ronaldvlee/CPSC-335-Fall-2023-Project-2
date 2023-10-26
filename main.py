from typing import List

# [𝑥,𝑦] attributes, where 𝑥 = numbers of trading stocks and 𝑦 = monetary value of the trading stocks

def stock_maximization_exhaustive(M: int, items: List[List[int]]) -> int:
    def maximize(index: int, remaining_M: int):
        if index < 0 or remaining_M <= 0: # base case if the index is out of bounds
            return 0, []                  # or no more money return an empty set
        
        number_of_included_stocks, included_stocks = 0, []
        quantity, value = items[index]

        if remaining_M >= value:
            number_of_included_stocks, included_stocks = maximize(index - 1, remaining_M - value)
            number_of_included_stocks += quantity
            included_stocks.append([quantity, value])

        number_of_excluded_stocks, excluded_stocks = maximize(index - 1, remaining_M)

        if number_of_included_stocks >= number_of_excluded_stocks:
            return number_of_included_stocks, included_stocks
        
        return number_of_excluded_stocks, excluded_stocks

    return maximize(len(items) - 1, M)

def stock_maximization_dynamic(M: int, items: List[List[int]]) -> int:
    return

stock_list = [ [1, 2], [4, 3], [3, 6], [6, 7]]
total_investment = 12
max_stocks, selected_stocks = stock_maximization_exhaustive(total_investment, stock_list)
print('-------------EXHAUSTIVE-------------')
print(f"Maximum number of stocks: {max_stocks}")
print(f"Selected stocks: {selected_stocks}")
print('\n')
print('-------------DYNAMIC----------------')


print('\n')
