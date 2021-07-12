score = []
for i in range(0, 10):
    i = int(input("점수 : "))
    if(0<=i<=100):
        score.append(i)
    else:
        print("에러")


for ii in range(0, 9):
    for jj in range(ii, 9):
        if (score[jj] > score[jj+1]) :
            a = score[jj]
            score[jj] = score[jj+1]
            score[jj+1] = a

# 버블 정렬

print(score)
