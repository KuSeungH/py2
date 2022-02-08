#ex02.py
# 문자열 인덱싱과 슬라이싱

# 문자열은 글자가 한줄로 나열되어 있는 형태이다
# 문자열은 각 글자는 순변을 매길 수 있다

#       0         1         2
#       0123456789012345678901234
str1 = 'He said. "I am a teacher"'
print(str1)
print(str1[0], str1[4], str1[-8], str1[12], str1[17])

# 문자열의 인덱스를 이용하여 
# 특정지점을 잘라내서 새로운 문자열로 가져온다
# 문자열의 슬라이싱
print(str1[17:23])  # 마지막 번호는 범위에 포함하지 않는다


today = '20220113sunday'
year = today[:4]
month = today[4:6]
date = today[6:8]
day = today[8:]
form = '오늘은 {}년 {}월 {}일 {}입니다'
print(form.format(year, month, date, day))
print()

idNumber = '980905-1345678'
num1 = idNumber.split('-')[0]
num2 = idNumber.split('-')[1]
birthYear = num1[:2]
birthMonth = num1[2:4]
birthDate = num1[4:]
gender = num2[0]
gender = int(gender) % 2 == 0 and '여성' or '남성'
form = '{}년 {}월 {}일 출생 {}입니다'
form = form.format(birthYear, birthMonth, birthDate, gender)
print(form)

# split(sp) : 지정한 글자를 기준으로 문자열을 분리하기