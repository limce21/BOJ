import sys
n = int(sys.stdin.readline())

stack_arr = []
n_arr = []
z = 1

flag = 0
for i in range(n):
    num = int(sys.stdin.readline())
    while z <= num:
        stack_arr.append("+")
        n_arr.append(z)
        z += 1
    if n_arr[-1] == num:
        stack_arr.append("-")
        n_arr.pop()
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in stack_arr:
        print(i)
