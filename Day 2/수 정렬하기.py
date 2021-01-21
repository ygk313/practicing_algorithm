N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()
for i in numbers:
    print(i)