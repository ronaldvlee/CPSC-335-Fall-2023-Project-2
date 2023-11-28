from project2 import stock_maximization_dynamic, stock_maximization_exhaustive
from parse_input import parse_input

with open('output.txt', 'w') as file: # creates a new empty output file
    pass

data = parse_input('input.txt')

for portfolio in data:
    stock_list, total_investment = portfolio

    max_stocks_e, selected_stocks_e = stock_maximization_exhaustive(total_investment, stock_list)
    max_stocks_d, selected_stocks_d = stock_maximization_dynamic(total_investment, stock_list)

    with open('output.txt', 'a') as file:
        file.write(f"--- stock list: {stock_list}; budget: {total_investment} ---\n")
        file.write(f"Exhaustive Max: {max_stocks_e}\n")
        file.write(f"Dynamic Max: {max_stocks_d}\n\n")

# stock_list = [ [1, 2], [4, 3], [3, 6], [6, 7]]
# total_investment = 10

# print('-------------EXHAUSTIVE-------------')
# max_stocks, selected_stocks = stock_maximization_exhaustive(total_investment, stock_list)
# print(f"Maximum number of stocks: {max_stocks}")
# print(f"Selected stocks: {selected_stocks}")
# print('\n')


# print('-------------DYNAMIC----------------')
# max_stocks, selected_stocks = stock_maximization_dynamic(total_investment, stock_list)
# print(f"Maximum number of stocks: {max_stocks}")
# print(f"Selected stocks: {selected_stocks}")
# print('\n')
