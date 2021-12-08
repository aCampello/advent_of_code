import numpy as np

with open('input_7.txt', 'r') as f:
    positions = [int(n) for n in f.read().split(',')]

# Part A
# The number that minimises the absolute distances to it is 
# called the median in maths (one can show that)

fuel = np.sum(np.abs(np.array(positions)-np.median(positions)))
print(fuel)

# Part B
# Maybe there is a mathematical formula for that full value
# but I am not sure. I will try brute force, computing the arithmetic sums

def arithmetic_sum(j):
    return j*(j+1)/2

best_fuel = 10**12

for n in range(max(positions)):
    fuel = np.sum([arithmetic_sum(np.abs(p-n)) for p in positions])
    if fuel < best_fuel:
        best_fuel = fuel
        best_pos = n

print(best_fuel)
print(best_pos)
