num_1 = 1
num_2 = 1
i = 1
while i <= 50:
    print(num_1)
    temp = num_1
    num_1 = num_2
    num_2 = temp + num_1
    i += 1
d