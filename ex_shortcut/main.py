# 제곱근 사용을 위한 sqrt 함수
from math import sqrt


# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)


# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    index_coordinates = len(coordinates)
    max_distance = 0
    _i = 0
    _j = 0
    for i in range(index_coordinates):
        for j in range(i + 1, index_coordinates):
            _distance = distance(coordinates[i], coordinates[j])

            if max_distance == 0:
                max_distance = _distance

            if _distance < max_distance:
                _i = i
                _j = j
                max_distance = _distance

    return [coordinates[_i], coordinates[_j]]


# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))


# Solution
def closest_pair2(coordinates):
    # 현재까지 본 가장 가까운 두 매장
    pair = [coordinates[0], coordinates[1]]

    for i in range(len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            store1, store2 = coordinates[i], coordinates[j]

            # 더 가까운 두 매장을 찾으면 pair 업데이트
            if distance(pair[0], pair[1]) > distance(store1, store2):
                pair = [store1, store2]

    return pair