# 사전 (dictionary)
# key-value pair (키-값 쌍)
my_dictionary = {
    5: 25,
    2: 4,
    3: 9
}

print(my_dictionary[3])
my_dictionary[9] = 81
print(my_dictionary)

# value 값 보기
print(my_dictionary.values())
print(5 in my_dictionary.values())

for value in my_dictionary.values():
    print(value)

# key 값 보기
print(my_dictionary.keys())

for key in my_dictionary.keys():
    value = my_dictionary[key]
    print(key, value)

print()
# key와 value 한번에 가져오기
for key, value in my_dictionary.items():
    print(key, value)
