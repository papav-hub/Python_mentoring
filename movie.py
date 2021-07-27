name = input("이름 : ")
print("*-"*30 + "*")
menu = 0

seat1 = []    # 빈 리스트 생성
for i in range(5):
    line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(5):
        line.append("O")     # 안쪽 리스트에 0 추가
    seat1.append(line)         # 전체 리스트에 안쪽 리스트를 추가

seat2 = []    # 빈 리스트 생성
for i in range(10):
    line = []              # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(10):
        line.append("O")     # 안쪽 리스트에 0 추가
    seat2.append(line)         # 전체 리스트에 안쪽 리스트를 추가



while(menu != 3):
    print("\t \t %s's 영화 예매기!" %(name))
    print("1. 마녀배달부 키키 : 프리미엄 상영관")
    print("2. 타이타닉 : 일반 상영관")
    print("3. 예매 그만하기")
    print("*-"*30 + "*")

    menu = int(input("주문할 상품의 번호를 입력해 주세요! : ")) # 영화 선택
    n = []


    if(menu == 1) : # 상영관에 따른 좌석수 변경
        n = seat1
    elif(menu == 2) :
        n = seat2
    print(n)



    c = int(input("좌석의 열 번호를 입력해 주세요! : "))
    l = int(input("좌석의 행 번호를 입력해 주세요! : "))

    if(n[c][l] == "O"):
        print("예매 완료!")
        n[c][l] = "X"
        print(n)
        
    else:
        print("이미 예매된 좌석입니다.")
    


    if(menu == 1) : # 다시 대입
        seat1 = n
        print(seat1)
    elif(menu == 2) :
        seat2 = n
        print(seat2)


