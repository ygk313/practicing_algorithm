cnt = 1
stack, result = [], []

N = int(input())

for _ in range(1, N+1):
    data = int(input())

    while cnt <= data:
        stack.append(cnt)
        cnt+=1
        result.append('+')
    
    if stack[-1] == data:
        stack.pop()
        result.append('-')
    #내림차순이 지켜지지 않은 경우
    else:
        print("NO")
        exit(0)

print("\n".join(result))