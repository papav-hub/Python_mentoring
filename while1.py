name = input("이름 : ")
print("*-"*30 + "*")
print("\t \t %s's REPEAT CALC PROGRAM" %(name))
print("*-"*30 + "*")

repeat = int(input("몇 번 반복할까요? : "))
count = 1
while(repeat > 0):
    print("%d번 반복 중입니다..." %(count))
    a = int(input("첫번째 인자 : "))
    b = int(input("두번째 인자 : "))

    print("a + b = %d" %(a+b))
    print("a - b = %d" %(a-b))
    print("a * b = %d" %(a*b))
    print("a / b = %d" %(a/b))
    print("제곱 : %d" %(a**b))
    print("a %" + "b = %d" %(a%b))
    print("몫 :  %d" %(a//b))

    repeat -= 1
    count += 1
    print("\n")