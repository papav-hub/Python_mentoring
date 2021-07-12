# 아무꺼나 돌려보기
print(1)
print(1+2)

# 정수형
a1 = 123
print(a1)

# 실수형
a2 = 1.2
print(a2)

# 연산자
print(float(a1 + a2))


# 문자열
a3 = "asdf"
print(a3)

# 이스케이프 코드
print("asdf\nasdf")

# 문자열 연산
b1 = "apple"
b2 = "banana"
print(b1 + b2)

# 문자열 곱셈
print(b1 * 2)

# 문자열 길이
print(len(b1))

# 인덱싱 & 슬라이싱
print(b1[1])
print(b1[1:3])
print(b1[:3])
print(b1[1:])

# 문자열 포매팅
print("I love %s" %(b1))


# 추가
print(b1.upper())
print(b1.replace("a", "b"))
print(b1.find('p'))
print(b1.count('p'))