N = int(input())
numbers = [tuple(map(int, input().split()))for _ in range(N)]

numbers.sort(key=lambda x: (x[0], x[1]))

for i,v in numbers:
    print(i,v)