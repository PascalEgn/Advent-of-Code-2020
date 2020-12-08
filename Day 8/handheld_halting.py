import copy

with open('input', 'r') as input_line:
    instruction_list = [line.rstrip().split() for line in input_line]

for index, _ in enumerate(instruction_list):
    modified_instructions = copy.deepcopy(instruction_list)
    if modified_instructions[index][0] == 'jmp':
        modified_instructions[index][0] = 'nop'
    elif modified_instructions[index][0] == 'nop':
        modified_instructions[index][0] = 'jmp'
    if modified_instructions != instruction_list:
        accumulator = 0
        current_index = 0
        visited_indices = []
        while current_index not in visited_indices and current_index < len(instruction_list):
            visited_indices.append(current_index)

            if modified_instructions[current_index][0] == 'acc':
                accumulator += int(modified_instructions[current_index][1])
                current_index += 1

            elif modified_instructions[current_index][0] == 'jmp':
                current_index += int(modified_instructions[current_index][1])

            elif modified_instructions[current_index][0] == 'nop':
                current_index += 1

        if current_index >= len(instruction_list):
            print(accumulator)
            break
