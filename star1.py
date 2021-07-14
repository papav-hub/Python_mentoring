n = 5
n = (n * 2) -1

for i in range(1, n+1, 2):
    j = int((n-i)/2)
    print(" " * j + "*" * i)

n = n - 2
for i in range(n, 0, -2):
    j = int((n-i)/2)
    print(" " * (j+1) + "*" * i)