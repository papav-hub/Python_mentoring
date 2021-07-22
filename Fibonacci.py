def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("몇 번째 수열까지 출력할까요?: "))

for i in range(1, n + 1):
    print(fibonacci(i))