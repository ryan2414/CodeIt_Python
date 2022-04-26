import random

# 목표 숫자 설정
target_number = random.randint(1, 20)

# 가능 횟수
life = 4

#
while life > 0:
    number = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(life)))

    if number > target_number:
        print("Down")
        life -= 1
    elif number < target_number:
        print("Up")
        life -= 1
    else:
        print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(life))
        break;

    if life <= 0:
        print("아쉽습니다. 정답은 {}입니다.".format(target_number))

# 모범 답안##################################
# 상수 정의
ANSWER = random.randint(1, 20)
NUM_TRIES =4

# 변수 정의
guess = -1
tries = 0

while guess != ANSWER and tries < NUM_TRIES:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(NUM_TRIES - tries)))
    tries += 1

    if ANSWER > guess:
        print("Up")
    else:
        print("Down")

if guess == ANSWER:
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(tries))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))

