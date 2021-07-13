name = input("이름 : ")
print("*-"*30 + "*")
print("\t \t %s's Ranking Program" %(name))
print("*-"*30 + "*")


score = [20, 30, 40, 10, 90, 80, 70, 60, 50]
myScore = int(input("나의 점수 : "))

score.append(myScore)
score.sort()
score.reverse()
ranking = score.index(myScore)

print("%s님의 등수는 : %d등" %(name, ranking))

