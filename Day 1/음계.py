v = list(map(int, input().split()))
a = list(range(1,9))
d = a[::-1]
print(a,d)

if a == v:
    print("ascending")
elif v == d:
    print("descending")
else:
    print("mixed")