def trapping_rain(buildings):
    # # heighest 를 갱신한다.
    # highest_building = 0
    # total_water = 0
    #
    # for index in range(len(buildings) - 1):
    #     if buildings[index] > highest_building:
    #         highest_building = buildings[index]
    #
    #     total_water += highest_building - buildings[index]
    #
    # return total_water
    building_sites = []
    remain_buildings = []
    rain = 0

    for height in buildings:
        building_sites += [int(height != 0)] # 빌딩 위치를 0과 1로 표시
        remain_buildings += [height - int(height != 0)] # 아래층부터 비의 양 계산하고 남은 빌딩 높이 리스트 저장

    for left_index in range(len(building_sites) -1 ):
        if building_sites[left_index] == 1:
            break

    for right_index in range(len(building_sites) - 1, 1, -1):  # 오른쪽부터 빌딩이 있는 곳 탐색
        if building_sites[right_index] == 1:
            break

    # 빌딩이 있는 구간 중 빌딩이 없는 곳을 게수하여 비의 양 계산

    if left_index + 1 < right_index:

        for index in range(left_index + 1, right_index):

            if building_sites[index] == 0:
                rain = rain + 1

    # 각 층별 빌딩위치와 비의 양 나타냄, (작동방식 이해돕는용)

    # print(building_sites, rain)

    # 비가 없는 층 부터는 계산 종료

    if rain == 0:
        return rain

    # 아래층부터 재귀적으로 계산

    return rain + trapping_rain(remain_buildings)

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))