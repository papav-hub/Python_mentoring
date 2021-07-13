name = input("이름 : ")
print("*-"*30 + "*")
print("\t \t %s's 구구단 PROGRAM 1" %(name))
print("*-"*30 + "*")

count = int(input("몇 단을 계산할까요? : "))

for i in range(1, 10):
    print("%d * %d = %d" %(count, i, count*i))