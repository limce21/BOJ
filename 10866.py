import sys
N = int(sys.stdin.readline())

dequeue = []
for i in range(N):
    string = list(map(str, sys.stdin.readline().split()))
    if string[0] == "push_front":
        dequeue.insert(0, int(string[1]))
    elif string[0] == "push_back":
        dequeue.append(int(string[1]))
    elif string[0] == "pop_front":
        if dequeue:
            print(dequeue[0])
            del dequeue[0]
        else:
            print(-1)
    elif string[0] == "pop_back":
        if dequeue:
            print(dequeue[-1])
            del dequeue[-1]
        else:
            print(-1)
    elif string[0] == "size":
        print(len(dequeue))
    elif string[0] == "empty":
        if dequeue == []:
            print(1)
        else:
            print(0)
    elif string[0] == "front":
        if dequeue:
            print(dequeue[0])
        else:
            print(-1)
    elif string[0] == "back":
        if dequeue:
            print(dequeue[-1])
        else:
            print(-1)
