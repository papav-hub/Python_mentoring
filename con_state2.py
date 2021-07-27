name = input("이름 : ")
print("*-"*30 + "*")
print("\t \t %s's 아이스크림 자판기!" %(name))
print("1. 딸기맛 : 1700원")
print("2. 초코맛 : 2900원")
print("3. 메론맛 : 3500원")
print("*-"*30 + "*")

menu = int(input("주문할 상품의 번호를 입력해 주세요! : "))
price = 0
if(menu == 1) :
    price = 1700
elif(menu == 2) :
    price = 2900
elif(menu == 3) :
    price = 3500
else :
    menu = int(input("입력 형식이 잘못되었습니다. 다시 입력해주세요 : "))



money = int(input("돈을 입금해주세요! : "))
while (money < price) :
    money = int(input("상품의 가격을 보고 다시 입금해 주세요: "))



# 거스름돈 돌려주기
remain = money - price

money_5000 = 0
money_1000 = 0
money_500 = 0

while(remain > 5000) :
    remain -= 5000
    money_5000 += 1

while(remain > 1000) :
    remain -= 1000
    money_1000 += 1

while(remain > 500) :
    remain -= 500
    money_500 += 1


print("<거스름돈>")
print("5000원 : %d장" %(money_5000))
print("1000원 : %d장" %(money_1000))
print("500원 : %d장" %(money_500))
print("나머지 : %d원" %(remain))

