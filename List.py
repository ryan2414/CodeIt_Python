# 리스트(list)
numbers = [2,3,5,7, 11,13]
names = ["윤수", "혜린", "태호", "영훈"]

# 인덱싱(indexing)
# 리스트에는 -indexing도 존재
print(numbers[-1])

# 리스트 슬라이싱 (List Slicing) [포함:미만]
print(numbers[0:4])
print(numbers[3:]) #4번재 부터 끝가지
print(numbers[:3]) #처음부터 3번째 항목까지

# 길이
print(len(numbers))

# 더하기 오른쪽에 들어간다
numbers.append(3)
print(numbers)

# 삭제
del  numbers[1]
print(numbers)

# 삽입
numbers.insert(4, 37)
print(numbers)

# 정렬 sorted > 기존 리스트는 건드리지 않고, 정렬된 새로운 리스트를 리턴
new_list = sorted(numbers)
print(new_list)
# 역정렬
new_list = sorted(numbers, reverse=True)
print(new_list)

# 정렬 sort > 아무것도 리턴하지 않고, 기존 리스트를 정렬 
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)