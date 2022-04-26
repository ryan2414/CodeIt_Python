total = 0
day = 31

with open("../data/chicken.txt", "r") as f:
    for line in f:
        split_line = line.strip().split(': ')
        total += int(split_line[1])

print(total / day)