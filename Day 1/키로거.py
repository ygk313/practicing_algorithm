T = int(input())

for _ in range(T):
    L = input()
    left, right = list(), list()

    for val in L:
        if val == "<":
            if left:
                right.append(left.pop())
        elif val == '>':
            if right:
                left.append(right.pop())
        elif val == '-':
            if left:
                left.pop()
        else:
            left.append(val)
    
    left.extend(reversed(right))
    print(left)