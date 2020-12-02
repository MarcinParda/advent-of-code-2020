def password_is_valid(line):
    splitted_line = line.split(" ")
    min = splitted_line[0].split("-")[0]
    max = splitted_line[0].split("-")[1]
    letter = splitted_line[1][0]
    letter_count = splitted_line[2].count(letter)
    if int(min) <= letter_count <= int(max):
        return True
    return False


def password_is_valid_2(line):
    splitted_line = line.split(" ")
    password = splitted_line[2]
    first_index = int(splitted_line[0].split("-")[0]) - 1
    second_index = int(splitted_line[0].split("-")[1]) - 1
    first_character = password[first_index]
    second_character = password[second_index]
    letter = splitted_line[1][0]
    if (first_character == letter) != (second_character == letter):
        return True
    return False


day2_input = open("day2_input", "r")

valid_count = 0
valid_count_2 = 0

for line in day2_input.read().split("\n"):
    if password_is_valid(line):
        valid_count += 1
    if password_is_valid_2(line):
        valid_count_2 += 1

print(valid_count, valid_count_2)
