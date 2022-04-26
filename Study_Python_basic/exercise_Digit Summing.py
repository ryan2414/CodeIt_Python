# 자리수 합 리턴
def sum_digit(num):
    # 코드를 입력하세요.
    str_num = str(num)
    len_num = len(str_num)
    value = 0
    for index in range(0, len_num):
        value += int(str_num[index])
    return value


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# 코드를 입력하세요.
total = 0
for num in range(1, 1001):
    total += sum_digit(num)

print(total)



def better_sum_digit(num):
    total = 0
    str_num = str(num)

    for digit in str_num:
        total += int(digit)

    return total
