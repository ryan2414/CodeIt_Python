def mask_security_number(security_number):
    # 코드를 입력하세요.
    len_security_number = len(security_number)
    masked_securty_number = ""
    for index in range(len_security_number):
        num = security_number[index]
        if index >= len_security_number - 4:
            num = '*'
        masked_securty_number += num

    return masked_securty_number


# 테스트
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))


def sample1(security_num):
    # security_num을 리스트로 변환
    # num_list = []

    num_list = list(security_num)

    # 마지막 네 값을 *로 대체
    # for i in range(len(security_num)):
    #     num_list.append(security_num[i])

    for i in range(len(num_list) - 4, len(num_list)):
        num_list[i] = "*"

    # 리스트를 문자열로 복구
    total_str = ""
    for i in range(len(num_list)):
        total_str += num_list[i]

    return total_str

def sample2(security_number):
    num_list = list(security_number)

    # 마지막 네 값을 *로 대체
    for i in range(len(num_list) -4, len(num_list)):
        num_list[i] = '*'

    # 리스트를 문자열로 복구하여 반환
    return ''.join(num_list)

def sampel3(security_number):
    return security_number[:-4] + '****'