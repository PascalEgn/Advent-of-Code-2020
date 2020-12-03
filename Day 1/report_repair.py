import numpy as np

with open('numbers', 'r') as number:
    number_list = [int(line.rstrip()) for line in number]


def get_prod_2(numbers):
    solution_numbers = set()
    for num1 in numbers:
        for num2 in numbers:
            if num1 + num2 == 2020:
                solution_numbers.add(num1)
                solution_numbers.add(num2)
                return list(solution_numbers)


def get_prod_3(numbers):
    solution_numbers = set()
    for num1 in numbers:
        for num2 in numbers:
            for num3 in numbers:
                if num1 + num2 + num3 == 2020:
                    solution_numbers.add(num1)
                    solution_numbers.add(num2)
                    solution_numbers.add(num3)
                    return list(solution_numbers)


print("Solution 1:")
print(np.prod(get_prod_2(number_list)))
print("-------------------------")
print("Solution 2:")
print(np.prod(get_prod_3(number_list)))
