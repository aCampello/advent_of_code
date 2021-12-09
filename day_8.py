with open('input_8.txt', 'r') as f:
    rows = [x.rstrip('\n') for x in f.readlines()]

n_segments_to_digit = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}


# Part A

easy_digits = 0

for row in rows:
    inputs, outputs = row.split(' | ')

    inputs = inputs.split(' ')
    outputs = outputs.split(' ')

    for segment in outputs:
         # If digit in segment, adds to easy digits
        easy_digits += bool(n_segments_to_digit.get(len(segment)))

print(easy_digits)


# Part B

original_combinations = {
    'abcefg': 0,  # Ok
    'cf': 1,  # Ok
    'acdeg': 2,  # Ok
    'acdfg': 3,  # Ok
    'bcdf': 4,  # Ok
    'abdfg': 5,  # Ok
    'abdefg': 6,  # Ok
    'acf': 7,  # Ok
    'abcdefg': 8,  # Ok
    'abcdfg': 9  #Ok
}

# The code below is disgusting. But the logic is as follows:
# # Find len = 2 -> This is 1
# ab = cf
# # Find len = 3 -> This is 7
# dab = acf -> d = a
# # Subtract both, the remaining letter is a
# # Find len = 4 -> This is 4
# eafb = bcdf
# # Find len = 6 with len = 4 substring len = 4 -> This is 9
# cefabd = abcdfg
# Find the strings which have 'acf' (Digit 7) as substring that haven't been decoded yet.
# If len == 6, it is 0
# If len == 5, it is 3
# Find remaining string with 6 letters, it is 6
# There are now two 5-letter segments remaining.
# The one that is a substring of 'abcdfg' (Digit 9) is
# 5. The remaining one is 2.

decoded_int = 0

for row in rows:
    inputs, outputs = row.split(' | ')

    inputs = inputs.split(' ')
    outputs = outputs.split(' ')

    decoded_input = [-1]*10
    decoded_output = [-1]*len(outputs)
    segment_to_digit = {}
    digit_to_segment = {}
    for i, segment in enumerate(inputs):
        if digit := n_segments_to_digit.get(len(segment)):
            decoded_input[i] = digit
            segment_to_digit["".join(sorted(segment))] = digit
            digit_to_segment[digit] = "".join(sorted(segment))
    # With this we find 4 digits. Now we find digit 9
    for i, segment in enumerate(inputs):
        sorted_segment = "".join(sorted(segment))
        if len(segment) == 6 and set(digit_to_segment[4]).issubset(set(sorted_segment)):
            decoded_input[i] = 9
            segment_to_digit["".join(sorted(segment))] = decoded_input[i]
            digit_to_segment[decoded_input[i]] = "".join(sorted(segment))

    for i, segment in enumerate(inputs):
        if decoded_input[i] == -1:
            sorted_segment = "".join(sorted(segment))
            if set(digit_to_segment[7]).issubset(set(sorted_segment)):
                if len(segment) == 6:
                    decoded_input[i] = 0
                elif len(segment) == 5:
                    decoded_input[i] = 3
            if decoded_input[i] != -1:
                segment_to_digit["".join(sorted(segment))] = decoded_input[i]
                digit_to_segment[decoded_input[i]] = "".join(sorted(segment))

    for i, segment in enumerate(inputs):
        if decoded_input[i] == -1:
            sorted_segment = "".join(sorted(segment))
            if len(segment) == 6:
                decoded_input[i] = 6
                segment_to_digit["".join(sorted(segment))] = decoded_input[i]
                digit_to_segment[decoded_input[i]] = "".join(sorted(segment))

    for i, segment in enumerate(inputs):
        if decoded_input[i] == -1:
            sorted_segment = "".join(sorted(segment))
            if len(segment) == 5 and set(sorted_segment).issubset(set(digit_to_segment[9])):
                decoded_input[i] = 5
                segment_to_digit["".join(sorted(segment))] = decoded_input[i]
                digit_to_segment[decoded_input[i]] = "".join(sorted(segment))

    for i, segment in enumerate(inputs):
        if decoded_input[i] == -1:
            sorted_segment = "".join(sorted(segment))
            decoded_input[i] = 2
            segment_to_digit["".join(sorted(segment))] = decoded_input[i]
            digit_to_segment[decoded_input[i]] = "".join(sorted(segment))

    for i, output in enumerate(outputs):
        decoded_output[i] = segment_to_digit["".join(sorted(output))]

    decoded_int += int("".join([str(x) for x in decoded_output]))

print(decoded_int)
