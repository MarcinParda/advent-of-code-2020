def finding_entries(numbers, sum):
    for first_number in numbers:
        for second_number in numbers:
            if first_number + second_number == sum:
                return first_number * second_number

day1_input = open("day1_input", "r")
lines = day1_input.read().split('\n')
numbers = []

for line in lines:
    numbers.append(int(line))

answer = finding_entries(numbers, 2020)
print(answer)
