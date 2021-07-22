name = input("이름 : ")
print("*-"*30 + "*")
print("\t \t %s's LeapYear Program" %(name))
print("*-"*30 + "*")


while(True):

    year = int(input("연도 : "))

    if (year % 4 == 0) and (year % 100 != 0) :
        print("%s년은 윤년입니다." %(year))
    elif (year % 400 == 0) :
        print("%s년은 윤년입니다." %(year))
    else :
        print("%s년은 윤년이 아닙니다." %(year))