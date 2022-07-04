import sys

N = int(sys.stdin.readline())
A = []
for i in range(N):
   A.append(int(sys.stdin.readline()))
   
A.sort()
print('\n'.join(map(str, A)))