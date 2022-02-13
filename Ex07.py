# ex07.py
# 비교 연산자를 활용하는 코드

# 1) 성인/미성년자 구분

age = int(input('나이입력 : '))
result1 = age >= 20 and '성인' or '미성연자'
print(result1)

# 2) 합격/불합격 구분
score = int(input('점수입력 : '))
if score >= 60:
    print('합격')
else:
    print('불합격')

# 3) 입력한 문자열 일치여부로 로그인 처리 예시
import getpass
id = 'itbank'
pw = 'it'
print()
print('로그인 테스트')
uesrid = input('ID : ')
userpw = input('PW : ')
uesrpw =getpass.getpass('pw : ')
if id == uesrid:
    if pw == userpw:
        print('로그인 성공')
    else:
        print('비밀번호가 일치하지 않습니다')
else:
    print('계정이 존재하지 않습니다')
