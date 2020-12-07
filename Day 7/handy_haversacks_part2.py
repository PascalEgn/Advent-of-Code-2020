import re


def get_rules(input_rules):
    found_rules = {}
    for input_line in input_rules:
        values = []
        key = re.match(r'^(\w*\s\w*)', input_line).group(1)
        for bag in input_line.split(','):
            bag_match = re.search(r'(\d\s\w*\s\w*)', bag)
            if bag_match:
                values.append(bag_match.group(1))
        found_rules[key] = values
    return found_rules


def count_bags(color, bags):
    bags_needed = 1
    for bag in bags[color]:
        bag_color = re.search(r'(\d)\s(\w*\s\w*)', bag)
        bags_needed += int(bag_color.group(1)) * count_bags(bag_color.group(2), bags)

    return bags_needed


input_file = open('input', 'r')

rules = get_rules(input_file)

print(rules)

search_color = 'shiny gold'
## -1 because we dont want to count the shiny gold bags itself
print(count_bags(search_color, rules)-1)
