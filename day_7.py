import numpy as np

with open('input_7.txt', 'r') as f:
    positions = [int(n) for n in f.read().split(',')]

# Part A
# The number that minimises the absolute distances to it is 
# called the median in maths (one can show that)

fuel = np.sum(np.abs(np.array(positions)-np.median(positions)))
print(fuel)

# Part B
# The  number integer that minimizes the arithmetic distances to it
# is called "arithmetic mean". We have to test ceil and floor however,
# because we're approximating by an integer

def arithmetic_sum(j):
    return j*(j+1)/2

best_pos = np.mean(positions)

fuel_1 = np.sum(arithmetic_sum(np.abs(positions-np.ceil(best_pos))))
fuel_2 = np.sum(arithmetic_sum(np.abs(positions-np.floor(best_pos))))
print(min(fuel_1, fuel_2))

