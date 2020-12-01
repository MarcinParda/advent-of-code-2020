def two_entries_multiplier(numbers, sum):
    i = 0
    while i < len(numbers):
        j = i + 1
        if numbers[i] < 2020:
            while j < len(numbers):
                if numbers[i] + numbers[j] == sum:
                    return numbers[i] * numbers[j]
                j += 1
        i += 1


def three_entries_multiplier(numbers, sum):
    i = 0
    while i < len(numbers):
        j = i + 1
        if numbers[i] < 2020:
            while j < len(numbers):
                if numbers[i] + numbers[j] < 2020:
                    k = j + 1
                    while k < len(numbers):
                        if numbers[i] + numbers[j] + numbers[k] == sum:
                            return numbers[i] * numbers[j] * numbers[k]
                        k += 1
                j += 1
        i += 1


day1_input = open("day1_input", "r")
lines = day1_input.read().split('\n')
numbers = []

for line in lines:
    numbers.append(int(line))

part1_answer = two_entries_multiplier(numbers, 2020)
part2_answer = three_entries_multiplier(numbers, 2020)

print(part1_answer)
print(part2_answer)
