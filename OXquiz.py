quiz = input("채점표를 입력하세요 : ")

quiz = quiz.upper()

score = 0
s = []

if(quiz[0]=="O"):
    s.append(1)
    score += 1
else:
    s.append(0)

for i in range(1, len(quiz)):
    if(quiz[i]=="O"):
        s.append(s[i-1] + 1)
        score += s[i-1] + 1
    else:
        s.append(0)


print(score)


