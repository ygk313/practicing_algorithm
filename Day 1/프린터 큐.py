TC = int(input())

for _ in range(TC):
    N,M = list(map(int, input().split()))
    V = list(map(int, input().split()))

    tmp = list()
    cnt= 0

    maxi = max(V)
    tmp = [val for val in enumerate(V)]

    while True:
        if tmp[0][1] == maxi:
            if M == tmp[0][0]:
                cnt+=1
                break
            tmp.pop(0)
            cnt += 1
        else:
            val = tmp.pop(0)
            tmp.append(val)
        
        maxi = max([v for i,v in tmp])
    
    print(cnt)
    