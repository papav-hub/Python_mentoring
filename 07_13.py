# 1차원 배열
list1 = [1, 3, 5, 7]
list2 = ['apple', 'banana', 'lemon']
print(list1[0])
print(list1[0] + list1[1])
print(list1[-1])


# 2차원
list3 = [1, 2, ['apple', 'banana']]
print(list3[2][0])


# 리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

a * 3 = [1, 2, 3, 1, 2, 3, 1, 2, 3]


# 리스트 길이
len(a)


# 리스트 수정
a[1] = 10


# 리스트 요소 삭제
del a[0]
del a[2:]


# 리스트에 요소 추가
a = [1, 2, 3, 5, 6]
a.append(4)
print(a)


# 특정 위치에 요소 삽입
a.insert(0, 4)


# 리스트 정렬
a.sort()


# 리스트 뒤집기
a.reverse()


# 위치 반환
a.index(3)


# 포함된 개수
a.count(4)




## if-elif-else
fruit = True
if fruit :
  print("과일 먹기")
else:
  print("굶기")


fruit = "사과"
if fruit=="사과":
  print("사과 먹기")
else:
  print("굶기")


score = 70
if (score == 100) :
  print("A+")
elif (score > 70) :
  print("B")
elif (score > 50) :
  print("C")
else :
  print("F")


fruit = True
fork = True
if(fruit and fork):
  print("포크로 과일 먹기")
else :
  print("굶기")


a = ["사과", "바나나"]
if("사과" in a) :
  print("사과 먹기")