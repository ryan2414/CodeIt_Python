i = 120
j = 1;
count = 0

while i >= j:
    if (i % j == 0):
        print(j)
        count += 1

    j += 1

print("{}의 약수는 총 {}개입니다.".format(i, count))