from random import randint


def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return  numbers

def draw_winning_numbers():
    # nomal_numbers = generate_numbers(6)
    # nomal_numbers.sort()
    # bonus_number = generate_numbers(1)
    # nomal_numbers.append(bonus_number[0])
    # print(nomal_numbers)
    winning_nubers = generate_numbers(7)
    return sorted(winning_nubers[:6]) + winning_nubers[6:]

def count_matching_numbers(list_1, list_2):
    correct_count = 0
    for number in list_1:
        if number in list_2:
            correct_count += 1

    return correct_count

def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count ==1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    else:
        return 5000

