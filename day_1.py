import pandas as pd

input_data = pd.read_csv('input.txt', header=None)

def calculate_n_increase(dataframe_col):
    return (dataframe_col[1:] - dataframe_col.shift(1)[1:] > 0).sum()

# Part A
print(calculate_n_increase(input_data[0]))

# Part B
rolling_data = input_data.rolling(3).sum()

print(calculate_n_increase(rolling_data[0]))
