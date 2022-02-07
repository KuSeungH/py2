# day01/ex01.py
# 문자열 포매팅 기능    {}



name = '구승현'
age = 25

print('{}는 나이는 {}살입니다'.format(name, age))
print('{:s}의 나이는{:d}살입니다'.format(name, age))    

# 데이터의 형태에 따라 상세한 서식을 지정하고 싶을 때
# 아매리카노 1,500원
# 몸무게 : 60.25 kg

# {:s} : string, 문자열
# {:d} : decimal, 10진수 (정수)
# {:f} : float, 실수

print()     # 내용이 없는 print() 는 한줄을 내린다
# print('ㅣ{:<25s}ㅣ'.format('메뉴판'))
# print('ㅣ{:>25s}ㅣ'.format('메뉴판'))
# print('ㅣ{:^25s}ㅣ'.format('메뉴판'))

print('ㅣ{:=^25s}ㅣ'.format(' 메뉴판 '))
print('{:5s}\t : {:10,d}원'.format('아메리카노', 1500))
print('{:5s}\t : {:10,d}원'.format('월드콘', 1800))
print('{:5s}\t : {:10,d}원'.format('초밥세트', 25000))
print()

kor = 100
eng = 99
math = 87
total = kor + eng + math
avg = total / 3 
print('{}님의 평균은 {:.2f}점'.format(name, avg))
print()

hour = 9
minute = 46
print('현재 시간은 {:02d} : {:02d}입니다'.format(hour, minute))
print()

year = 2022
month = 1
date = 12
print('오늘 날짜 : {}-{:02d}-{:02d}'.format(year, month, date))
print()

# 문자열 포매팅은 반드시 출력에만 사용하는 것이 아니다!!
# 1) 서식만 미리 정해둔다
today = '{}-{:02d}-{:02d} {:02d}:{:02d}:{}'

# 2) 서식에 값을 채워넣어서 다시 변수에 저장
today = today.format(year, month, date, hour, minute, 2)

# 3)서식과 값이 준비된 변수값을 출력
print(today)
print()
