"""name = input("이름 : ")
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
print("나머지 : %d원" %(remain))"""



# 프로그램 제목 출력
# 메뉴판 출력
# 입금한 돈 구매품목,구매수량을 입력받을 때, 가이드 텍스트 출력하기
# 주문한 금액이 입금한 금액보다 많으면 예외처리
# 주문한 금액을 빼고 거스름돈을 돌려준다. ( 5000, 1000, 500, 100)
# 문자열 포매팅 사용

#재고량 + 구매수량 추가
name = input("이름을 입력하세요 : ")
print("**"*24 + "*")
print(" \t   %s의 E동 5층의 자판기\t\t" % name)
drink = [["1. 콜라 : 1000원",1000,10], ["2. 스프라이트 : 600원",600,10], ["3. 오렌지주스 : 500원",500,10], ["4. 코코팜화이트 : 700원",700,10],
         ["5. 토레타 : 1300원",1300,10], ["6. 코코팜 : 700원",700,10], ["7. 식혜 : 600원",600,10], ["8. 유자차 : 600원",600,10]]
    

print("**"*24 + "*")
print("\n")

won = [["5000원",0],["1000원",0],["500원",0],["100원",0]]



# 돈 입력받기
sub = int(input("돈을 투입구에 투입해주세요 : "))
#예외처리 1 ) 100원미만의 금액 받지않기
if(sub%100 != 0):
    print("100원 미만의 금액단위는 받지 않습니다.")
    print("%d원 출력" %sub)
    exit(1)
while(True):
    print("**"*24 + "*")
    print(" \t   %s의 E동 5층의 자판기\t\t" % name)
    for i in range(0, len(drink)):
        print("%s || 재고량 : %d 개" % (drink[i][0],drink[i][2]))
    print("**"*24 + "*")
    select = int(input("상품을 주문하려면 ' 1 ', 잔돈을 출력하려면 ' 2 '를 입력하세요 : "))
    
    print("\n")
    if(select==1):
        # 상품 번호 입력받기
        num = int(input("주문할 상품의 번호를 입력해주세요! : "))
        #예외처리 2 ) 재고량 부족
        if(drink[num-1][2] == 0): 
            print("error : 재고량이 부족합니다.")
            break
        count = int(input("주문할 상품의 개수를 입력하세요 : "))
        #예외처리 3 ) 입력개수가 현재 재고량보다 많은 경우
        if(drink[num-1][2] < count):
            print("error : 재고량이 부족합니다.")
            break
        #예외처리 4 ) 음료개수를 0개 이하로 입력한 경우
        elif(count <=0):
            print("error : 1개 이상의 음료를 입력하세요.")
            break
        #예외처리 5 ) 현재 돈 - 음료가격이 0보다 작은 경우
        if((sub - (drink[num-1][1])*count )< 0): 
            print("error : 돈이 부족합니다.")  # 에러문구 출력
            print("%d원을 출력합니다." %sub)
            break  # 실행즉시종료
        # sub 변수에 현재 돈 - 음료가격 값 저장
        sub = sub - (drink[num-1][1])*count 
        drink[num-1][2]-=count # 개수 차감
        # 돈 입력액수 - 상품의 가격
        
    elif(select!=1):
        break

    print("남은 금액은 %d 입니다." % sub)
    

#잔돈계산하자
while(sub > 0):
    if(sub // 5000 != 0):
        won[0][1] += sub/5000  # 5천원 개수 출력
        sub = sub % 5000
    elif(sub // 1000 != 0):
        won[1][1] += sub/1000  # 1천원 개수 출력
        sub = sub % 1000
    elif(sub // 500 != 0):
        won[2][1] += sub/500  # 5백원 개수 출력
        sub = sub % 500
    else:
        won[3][1] += sub/100  # 1백원 개수 출력
        sub = sub % 100
    
        
#for문으로 잔돈출력
for k in range(0,4):
    print("%s : %d 장" %(won[k][0],won[k][1]))