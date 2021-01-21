N = int(input())
check = set(map(int, input().split()))

M = int(input())
tmp = list(map(int, input().split()))

for val in tmp:

    if val in check:
        print("1")
    else:
        print("0")