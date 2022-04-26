bank_seed_money = 50000000
apart = 1100000000

year = 1989

while year <= 2016:
    bank_seed_money += bank_seed_money * 0.12
    year += 1

if bank_seed_money > apart:
    print("{0:.0f}원 차이로 동일 아저씨 말씀이 맞습니다.".format(bank_seed_money - apart))
else:
    print("{0:.0f}원 차이로 미란 아주머니 말씀이 맞습니다.".format(apart - bank_seed_money - apart))