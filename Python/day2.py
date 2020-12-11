# Part 1

with open('../Input/day2_input.txt') as f:
    input = [line for line in f.read().splitlines()]

def split_string(line):
    min_val = int(line.split('-')[0])
    max_val = int(line.split('-')[1].split(' ')[0])
    letter = line.split('-')[1].split(' ')[1][0]
    password = line.split(':')[1][1:]
    return min_val, max_val, letter, password

count = 0
for line in input:
    min_val, max_val, letter, password = split_string(line)
    if min_val <= password.count(letter) <= max_val:
        count += 1
    
print(count)
    
# Part 2
def valid_password(idx_1, idx_2, char, password):
    return (password[idx_1-1] == char) != (password[idx_2-1] == char)

valid_passes = [valid_password(*split_string(line)) for line in input]
print(sum(valid_passes))


