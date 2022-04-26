# 오늘은 2022년 04월 21일 입니다.
year = 2022
month = 4
day = 21

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")
print("오늘은 {1}년 {0}월 {2}일입니다.".format(year, month, day))
date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1/num_2))
# {2:.2f} //소수점 2번째 자리까지 Sorting

print(type(3))
print(type(3.0))
print(type("3"))