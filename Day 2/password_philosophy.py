import re

passwords = open('input', 'r')
correct_passwords = 0

for password in passwords:
    match = re.match(r'(\d*)-(\d*)\s(\w):\s(\w*)', password)
    char_amount = match.groups()[3].count(match.groups()[2])
    if int(match.groups()[0]) <= char_amount <= int(match.groups()[1]):
        correct_passwords += 1

print("Solution 1:")
print(correct_passwords)
print("-------------------------")
passwords = open('input', 'r')
correct_passwords = 0


for password in passwords:
    match = re.match(r'(\d*)-(\d*)\s(\w):\s(\w*)', password)
    if match.groups()[3][int(match.groups()[0])-1] == match.groups()[2] and match.groups()[3][int(match.groups()[1])-1] != \
            match.groups()[2]:
        correct_passwords += 1
    if match.groups()[3][int(match.groups()[1])-1] == match.groups()[2] and match.groups()[3][int(match.groups()[0])-1] != \
            match.groups()[2]:
        correct_passwords += 1

print("Solution 2:")
print(correct_passwords)
