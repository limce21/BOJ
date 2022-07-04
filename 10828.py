import sys
N = int(sys.stdin.readline())

stack = []
for i in range(N):
    string = list(map(str, sys.stdin.readline().split()))
    if string[0] == "push":
        stack.append(int(string[1]))
    elif string[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif string[0] == "size":
        print(len(stack))
    elif string[0] == "empty":
        if stack == []:
            print(1)
        else:
            print(0)
    elif string[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
