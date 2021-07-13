name = input("이름 : ")
print("*-"*30 + "*")
print("\t \t %s's 학기 성적 프로그램!" %(name))
print("*-"*30 + "*")


grade = []
subject = ["국어", "수학", "사회", "과학"]

for s in subject :
    score = int(input("%s 점수 : " %(s)))

    while (score < 0 or score > 100) :
        score = int(input("%s 점수 다시 입력 : " %(s)))
    
    if (score == 100) :
        grade.append("A")
    elif (score > 70) :
        grade.append("B")
    elif (score > 50) :
        grade.append("C")
    else :
        grade.append("F")

print("\n")
print("<%s님의 이번학기 성적표>" %(name))
for i in range(0, len(subject)) :
    print("%s 과목 학점 : %s" %(subject[i], grade[i]))