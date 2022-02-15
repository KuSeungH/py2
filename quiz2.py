# quiz2.py
# 입력 함수 사용하는 문제

# 1) 올해 년도와 태어난 년도를 입력받아 현재 나이를 계산하세요
# 올해 : 2022
# 출생 : 1993
# 당신의 나이는 30살입니다

currentYear = int(input('올해 :'))
birthYear = int(input('출생'))
age = currentYear - birthYear + 1
print(' 당신의 나이는 {} 살입니다'.format(age))


# 2) 600kg 제한 화물 엘리이터가 있다
# 2개의 물건의 무게를 실수로 입력받고 
# 추가로 적재할 수 있는 무게를 계산해서 출력하도록 작성
# 첫번째 물건의 무게 : 123.34
# 두번째 물건의 무게 : 32.76
# 남은 무게 : 443.81 / 600.00kg


box1 = float(input('첫번째 물건의 무개 : '))
box2 = float(input('두번째 물건의 무게 : '))
availWeight = 600 - box1 - box2
print('남은 무게 : {:.2f}kg\n'.format(availWeight))


# 3) 이름과 나이를 입력받아서 한줄에 출력하기
# 당신의 이름은 무엇입니까 : 이지은
# 이지은님의 나이는 몇살입니까 : 30 
# 이지은님의 나이는 30살입니다

name = input('당신의 이름은 무것입니까 : ')
age = input('{}님의 나이는 몇살입니까 : '.format(name))
print(' {}님의 나이는 {}살입니다'.format(name, age))