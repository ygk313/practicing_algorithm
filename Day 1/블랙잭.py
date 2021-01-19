import sys

N,M = list(map(int, sys.stdin.readline().split()))
card = list(map(int, sys.stdin.readline().split()))
result = list()

for i in range(0, len(card)-2):
    for j in range(i+1, len(card)-1):
        for k in range(j+1, len(card)):
            if (card[i]+card[j]+card[k]) <= M:
                result.append(card[i]+card[j]+card[k])

print(max(result))