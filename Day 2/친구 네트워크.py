def find(node):
    if node == parent[node]:
        return node
    else:
        p = find(parent[node])
        parent[node] = p
        return parent[node]

def union(x,y):
    #find 함수는 루트 찾기하는 거
    x = find(x)
    y = find(y)

    if x!=y:
        parent[y] = x
        #x가 루트이니까
        number[x] += number[y]
TC = int(input())

for _ in range(TC):
    N = int(input())
    parent = dict()
    number = dict()

    for _ in range(N):
        x,y = input().split()

        if x not in parent:
            parent[x] = x
            number[x] = 1
        
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union(x,y)
        print(number[find(x)])

print(number.items())

