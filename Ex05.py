# ex05.py
# random 과 나머지 연산을 응용
# 파이썬 소스코드는 모듈이라고 부른다
# 다른 모듈을 불러와서 이미 만들어진 기능을 활용할 수 있다
# 파이썬 기본만 설치해도 제공되는 모듈이 많이 있다

import random # 파이썬에서 기본 제공하는 랜덤 관련된 모듈

while True:
    rand1 = random.randint(1, 6)
    # print('랜덤 수 : ', rand1)

    dice = rand1 % 6 + 1
    print('주사위 : ', dice)
    
    result = dice % 2 == 0 and '탈출' or '실패'
    print(result)

    if result == '탈출':
       break
print('탈출 성공 !!')