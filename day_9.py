import numpy as np

# Part A

l = []

n_rows = 0
with open('input_9.txt', 'r') as f:
    for line in f:
        n_rows += 1
        l.append(list(line[:-1]))

n_columns = len(l[0])

# M extends with a high number on the border
M = np.zeros((n_rows+2, n_columns+2))+1000

for i in range(n_rows):
    for j in range(n_columns):
        M[i+1][j+1] = l[i][j]


def is_low(i, j):
    if M[i, j] < M[i, j+1] and M[i, j] < M[i+1, j] and M[i, j] < M[i-1, j] and M[i, j] < M[i, j-1]:
        return True
    else:
        return False

low_points = []
risk = 0
for i in range(n_rows):
    for j in range(n_columns):
        if is_low(i+1, j+1):
            low_points.append((i+1, j+1))
            risk += M[i+1, j+1]+1

print(risk)

# Part B


def find_basin(i, j, visited=np.zeros_like(M)):
    visited[i][j] = 1

    if M[i, j] in [9, 1000]:
        return []
    basin_flow = []

    if not visited[i, j-1]:
        basin_flow += find_basin(i, j-1, visited=visited)
    if not visited[i-1, j]:
        basin_flow += find_basin(i-1, j, visited=visited)
    if not visited[i+1, j]:
        basin_flow += find_basin(i+1, j, visited=visited)
    if not visited[i, j+1]:
        basin_flow += find_basin(i, j+1, visited=visited)

    return basin_flow + [(i, j)]

lenghts = []
for point in low_points:
    basin = find_basin(point[0], point[1], visited=np.zeros_like(M))
    lenghts.append(len(basin))

sorted_3 = sorted(lenghts, reverse=True)[:3]
print(sorted_3)
print(np.prod(sorted_3))

