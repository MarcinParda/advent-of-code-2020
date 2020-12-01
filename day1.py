def two_entries_multiplier(numbers, sum):
    for first_number in numbers:
        for second_number in numbers:
            if first_number + second_number == sum:
                return first_number * second_number

def three_entries_multiplier(numbers, sum):
    for first_number in numbers:
        for second_number in numbers:
            if first_number + second_number < 2020:
                for third_number in numbers:
                    if first_number + second_number + third_number == sum:
                        return first_number * second_number * third_number


day1_input = open("day1_input", "r")
lines = day1_input.read().split('\n')
numbers = []

for line in lines:
    numbers.append(int(line))

part1_answer = two_entries_multiplier(numbers, 2020)
part2_answer = three_entries_multiplier(numbers, 2020)

print(part1_answer)
print(part2_answer)
