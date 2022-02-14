#quiz1.py

# 다음 문제를 읽고 계산식을 세워서 변수를 이용하여 결과를 출력하세요
# 출력시에는 문자열 포매팅을 적절하게 활용해보세요

# 1) 놀이공원을 가기 위해 11개의 지하철역을 지나왔다
# 출발역에서 도착역까지 37분이 걸렸다면 
# 한 역을 지나는데 걸리는 시간은 평균 얼마인지 출력하세요

stationCount = 11
elapsedTime = 37
averageTime =  elapsedTime / stationCount
print('한 역을 지나가는 평균 시간은 {:.2f}분 입니다'.format(averageTime))


# 2) 호텔 한층의 높이는 260cm 이다
# 총 14개의 층을 쓰고 있으며, 1층만 높이가 500.23cm 라면
# 이 건물의 높이는 총 몇 m 인가? (소수점 3자리까지 출력)

oneFloowHeight = 260
totalHeight = 14
firstFloorHeight = 500.23
plus = (oneFloowHeight * (totalHeight - 1) + firstFloorHeight) / 100
print('건물의  총 높이는 {:0.3f}m 이다'.format(plus))


# 3) 전동 자전거로 100m 를 이동하는데 11.27초가 걸렸다
# 같은 속력으로 이동하면 1시간 후 몇 km 이동할 수 있는가?
# (소수점 둘쨰자리까지 출력)

# 속력 = 거리 / 시간    (일정 시간 동안 얼마만큼 거리를 이동하는가) 

speed = 100 / 11.27
print(speed)    # m/s
                # km/h
print('1시간 후 전동자전거의 거리 : {:.2f}km'.format(speed * 60 * 60 / 1000))
# 1시간 = 60분 = 3600초
# 1km = 1000m
# go = 100
# time = 11.27
# total =  (60 / time) * go / 1000
# print('1시간 후에 총 {:0.2f}km 이동했다'.format(total))
