import numpy as np


def tree_encounters(starting_position, slope, pattern):
    tree_counter = 0
    pattern_column_size = len(pattern) - 1
    pattern_row_size = len(pattern[0])
    current_position = starting_position.copy()

    while current_position[0] < pattern_column_size:
        current_position[0] += slope[0]
        current_position[1] += slope[1]
        if current_position[1] >= pattern_row_size:
            current_position[1] = current_position[1] % pattern_row_size
        if pattern[current_position[0]][current_position[1]] == '#':
            tree_counter += 1

    return tree_counter


with open('input', 'r') as input_pattern:
    input_pattern = [line.rstrip() for line in input_pattern]

position = [0, 0]

slope_1 = [1, 1]
slope_2 = [1, 3]
slope_3 = [1, 5]
slope_4 = [1, 7]
slope_5 = [2, 1]

trees = [tree_encounters(position, slope_1, input_pattern),
         tree_encounters(position, slope_2, input_pattern),
         tree_encounters(position, slope_3, input_pattern),
         tree_encounters(position, slope_4, input_pattern),
         tree_encounters(position, slope_5, input_pattern)]

print(trees)
print(np.product(trees, dtype=np.int64))
