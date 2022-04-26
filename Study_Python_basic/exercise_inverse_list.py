numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
# 코드를 입력하세요.
for left in range(len(numbers)//2):
    right = len(numbers) - 1 - left

    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp


print("뒤집어진 리스트: " + str(numbers))



for left in range(len(numbers) //2):
    right = len(numbers) -1 - left

    numbers[right], numbers[left] = numbers[left], numbers[right]

print("뒤집어진 리스트: " + str(numbers))
