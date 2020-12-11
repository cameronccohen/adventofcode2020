import itertools

with open('../Input/day1_input.txt') as f:
    nums = [int(num) for num in f.read().splitlines()]

doubles = list(itertools.combinations(nums, 2))
triples = list(itertools.combinations(nums, 3))
def sums_to_2020(values):
    return sum(values) == 2020

sol1 = list(filter(sums_to_2020, doubles))
sol2 = list(filter(sums_to_2020, triples))

print(sol1)
print(sol2)