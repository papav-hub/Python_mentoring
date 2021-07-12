name = input("이름 : ")
print("*-"*30 + "*")
print("\t \t %s's Score Program" %(name))
print("*-"*30 + "*")


subject = input("과목 이름 : ")
score = int(input("점수 : "))
grade = ""


if (score == 100) :
    grade = "A"
elif (score > 70) :
    grade = "B"
elif (score > 50) :
    grade = "C"
else :
    grade = "F"

print("%s님의 %s과목 학점 : %s" %(name, subject, grade))