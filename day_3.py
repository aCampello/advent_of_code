import numpy as np

rows = []

with open('input_3.txt', 'r') as f:
    for row in f:
        rows.append([int(i) for i in list(row[:-1])])


report = np.array(rows)

# Part A
most_common_bits = [str(int(x)) for x in report.sum(axis=0) > len(report)/2]
least_common_bits = [str(1-int(x)) for x in most_common_bits]

print(most_common_bits)
print(least_common_bits)

power = int(''.join(most_common_bits), base=2)*int(''.join(least_common_bits), base=2)
print(f"Power: {power}")

# Part B

shortlist = report
pos = 0

while len(shortlist) > 1:
    most_common_bit = int(shortlist[:, pos].sum() >= len(shortlist)/2)
    shortlist = shortlist[shortlist[:, pos] == most_common_bit]
    pos += 1

print(shortlist)
oxygen = int(''.join([str(x) for x in shortlist[0]]), base=2)

shortlist = report
pos = 0

while len(shortlist) > 1:
    least_common_bit = 1-int(shortlist[:, pos].sum() >= len(shortlist)/2)
    shortlist = shortlist[shortlist[:, pos] == least_common_bit]
    pos += 1

co2 = int(''.join([str(x) for x in shortlist[0]]), base=2)

print(shortlist)
print(f"Life supply: {oxygen*co2}")
