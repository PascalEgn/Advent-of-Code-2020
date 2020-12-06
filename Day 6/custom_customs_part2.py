input_answers = open('input', 'r')

group_answers = []
groups = []

for line in input_answers:
    line = line.rstrip()
    if not line.strip():
        groups.append(group_answers.copy())
        group_answers.clear()
    else:
        group_answers.append(line)
groups.append(group_answers.copy())


answers_sum = 0

for group in groups:
    if len(group) == 1:
        answers_sum += len(group[0])
    else:
        for char in group[0]:
            char_counter = 0
            for answers in group[1:]:
                if answers.find(char) != -1:
                    char_counter += 1
            if char_counter == len(group)-1:
                answers_sum += 1

print(answers_sum)
