import sys
T = int(sys.stdin.readline())

for i in range(T):
    lst = list(sys.stdin.readline().strip())
    vps_list = []
    breakx = 0
    for j in range(len(lst)):
        if lst[j] == '(':
            vps_list.append(0)
        elif lst[j] == ')':
            if not vps_list:
                print("NO")
                breakx += 1
                break
            else:
                vps_list.pop()
    if breakx != 0:
        continue
    else:
        if vps_list:
            print("NO")
        else:
            print("YES")
