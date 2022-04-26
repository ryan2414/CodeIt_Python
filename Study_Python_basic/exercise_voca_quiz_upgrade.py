import random

with open('vocabulary.txt', 'r') as f:
    count = 0
    line_list = []
    for line in f:
        count += 1
        line_list.append(line)

    while True:
        rnd_num = random.randint(1, count - 1)
        split_line = line_list[rnd_num].strip().split(': ')
        eng_word = split_line[0]
        kor_word = split_line[1]

        answer = input("{}: ".format(kor_word))
        if eng_word == answer:
            print("맞았습니다!")
        elif answer == 'q':
            break;
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(eng_word))

# 모범답안 ########################
# 사전 만들기
vocab = {}
with open("vocabulary.txt", "r") as f:
    for line in f:
        data = line.strip().split(": ")
        eng_word, kor_word = data[0], data[1]
        vocab[eng_word] = kor_word

# 목록 가져오기
keys = list(vocab.keys())

# 문제 내기
while True:
    # 랜덤한 문제 받아오기
    index = random.randint(0, len(keys) - 1)
    eng_word = keys[index]
    kor_word = vocab[eng_word]

    # 유저 입력값 받기
    guess = input("{}: ".format(kor_word))

    # 프로그램 끝내기
    if guess == 'q':
        break

    # 정답 확인하기
    if guess == eng_word:
        print("정답입니다.\n")
    else:
        print("아쉽습니다. 정답은 {}입니다.\n".format(eng_word))

