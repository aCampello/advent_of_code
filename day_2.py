# Part 1

with open('input_2.txt', 'r') as f:
    pos = [0, 0]
    pos_add_dict = {'forward': [1, 0], 'up': [0, -1], 'down': [0, 1]}
    for line in f:
        direction, steps = line.split(' ')
        pos[0] += pos_add_dict[direction][0]*int(steps)
        pos[1] += pos_add_dict[direction][1]*int(steps)

print(pos)
print(pos[0]*pos[1])

# Part 2

with open('input_2.txt', 'r') as f:
    pos = [0, 0, 0] # Horizontal, Depth, Aim
    pos_add_dict = {'forward': [1, 0, 0], 'up': [0, 0, -1], 'down': [0, 0, 1]}
    for line in f:
        direction, steps = line.split(' ')
        pos[0] += pos_add_dict[direction][0]*int(steps)
        pos[1] += pos_add_dict[direction][1]*int(steps)
        pos[2] += pos_add_dict[direction][2]*int(steps)
        
        if direction == 'forward':
            pos[1] += pos[2]*int(steps)

print(pos)
print(pos[0]*pos[1])


