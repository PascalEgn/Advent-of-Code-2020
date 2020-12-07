import re


def get_rules(input_rules):
    found_rules = {}
    for input_line in input_rules:
        values = []
        key = re.match(r'^(\w*\s\w*)', input_line).group(1)
        for bag in input_line.split(','):
            bag_match = re.search(r'\d\s(\w*\s\w*)', bag)
            if bag_match:
                values.append(bag_match.group(1))
        found_rules[key] = values
    return found_rules


def search_for_color(color, bags):
    colors_found = set()
    for bag, contains in bags.items():
        if color in contains:
            colors_found.add(bag)
            colors_found.update(search_for_color(bag, bags))
    return colors_found


input_file = open('input', 'r')

rules = get_rules(input_file)


color_counter = 0

search_color = 'shiny gold'

print(len(search_for_color(search_color, rules)))



