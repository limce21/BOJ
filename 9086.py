import sys
T = int(sys.stdin.readline())
for i in range(T):
    string = sys.stdin.readline().strip()
    print(string[0]+string[-1])
