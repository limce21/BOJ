import sys
string_list = list(str(sys.stdin.readline()).strip())
N = len(string_list)
M = int(sys.stdin.readline())

right_cursor = []

for i in range(M):
    cmd = list(map(str, sys.stdin.readline().split()))
    if cmd[0] == 'L':
        if string_list:
            right_cursor.append(string_list.pop())
    elif cmd[0] == 'D':
        if right_cursor:
            string_list.append(right_cursor.pop())
    elif cmd[0] == 'B':
        if string_list:
            string_list.pop()
    elif cmd[0] == 'P':
        string_list.append(cmd[1])

string_list.extend(reversed(right_cursor))

for i in string_list:
    print(i, end="")
