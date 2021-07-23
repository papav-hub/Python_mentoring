a = int(input("A : ")) # 낮
b = int(input("B : ")) # 밤
v = int(input("V : ")) # 막대

k = 0	#올라가는 데 걸리는 일수
d = 0	#올라간 높이

while 1:
    k+=1
    if (a*k)-(b*(k-1))>=v:
        break
    
print(k)