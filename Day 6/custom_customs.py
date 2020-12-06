input_answers = open('input', 'r')

group_answers = set()
groups = []

for line in input_answers:
    line = line.rstrip()
    if not line.strip():
        groups.append(group_answers.copy())
        group_answers.clear()
    else:
        group_answers.update(*line)
groups.append(group_answers.copy())

answers_sum = 0

for group in groups:
    answers_sum += len(group)

print(answers_sum)
