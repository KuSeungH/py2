# ex06.py
# 연산자 (part2)

# 대입연산자 : 오른쪽의 값을 왼쪽에 복사하여 저장한다

a =1
b = 2
c, d = 3, 4     # 여러 변수에 동시에 값을 지정할 때

# 복합대입 연산자 : 산술연산의 결과를 다시 대입한다
print(a, b, c, d)
a = a + b

print(a, b, c, d)

a += b          # a = a + b
print(a, b, c, d)

b -= a
print(a, b, c, d)

c *= a
print(a, b, c, d)

d /= a  
print(a, b, c, d)

# 파이썬은 변수 선언시 자료형을  명시하지 않는다
# 기존에 정수를 가지고 있는 변수에 실수를 대입하면
# 변수의 자료형이 바뀐다
# (C, C++, Java 에서는 선언된 변수의 자료형이 바뀌지 않는다)

a //= b
print(a, b, c, d)

# 파이썬은 단항 증감 연산자가 없다 (++, --)
# 같은 기능을 수행하는  표현이 2개 이상일 필요가 없다

# 거듭제곱

print()
print(2 ** 0)  # 모든 수의 0승은 1
print(2 ** 1)
print(2 ** 2)
print(2 ** 3)
print(2 ** 4)
print(2 ** 5) 
print(2 ** 0.5) # 제곱근
print(3 ** 0.5)

#  비교 연산 : 크기 및 일치 여부를 비교하여 True 혹은  False로 값을 만근다
print(a > b)            # 크다, 초과
print(a < b)            # 작다, 미만
print(a >= b)           # 크거나 같다, 이상
print(a <= b)           # 작거나 같다, 이하
print(a == b)           # 일치한다
print(a != b)           # 일치하지 않는다
print(a is b )          # 일치한다
print(a is not b)       # 일치하지 않는다

# 리터럴과 변수간의 비교에서는 서로 다른 결과를 가진다
word1 = 'ITBANK'
word2 = input('ITBANK 라고 압력 :')

print('word1 == word2', word1 == word2)
# word1의 값과 word2의 값이 일치한다 (문자열도 연산자로 비교 가능)

print('word1 is word2', word1 is word2)
# word1이 바라보는 데이터와 word2가 바라보는 데이터는 동일한 곳이 아니다
# 서로 다른 곳의 데이터를 보고 있지만 두 데이터의 값이 일차하는 경우이다

# 경기도 광주와 전라도 광주는 
# 동알헌 이름을 가지지만 (값은 동일하지만)
# 서로 위치는 다르다 (가르키는 대상은 다르다)

