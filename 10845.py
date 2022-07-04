import sys
N = int(sys.stdin.readline())

queue = []
for i in range(N):
    string = list(map(str, sys.stdin.readline().split()))
    if string[0] == "push":
        queue.append(int(string[1]))
    elif string[0] == "pop":
        if queue:
            print(queue[0])
            del queue[0]
        else:
            print(-1)
    elif string[0] == "size":
        print(len(queue))
    elif string[0] == "empty":
        if queue == []:
            print(1)
        else:
            print(0)
    elif string[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif string[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
