import copy

def recursive(array, x): 
    if len(array) == x:
        tmp.append(copy.deepcopy(array))
        return
    
    array.append(' ')
    recursive(array, x)
    array.pop()
    
    array.append('+')
    recursive(array, x)
    array.pop()

    array.append('-')
    recursive(array, x)
    array.pop()

TC = int(input())

for _ in range(TC):
    tmp = list()

    x = int(input())
    nums = list(range(1,x+1))
    recursive([], x-1)

    for val in tmp:
        string = ""
        for i in range(x-1):
            string += str(nums[i]) + val[i]

        string += str(nums[-1])

        if eval(string.replace(" ", "")) == 0:
            # print(val)
            print(string) 
    print()


