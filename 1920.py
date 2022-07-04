import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

def isIn(x, A, start, end):
   while(start <= end):
      m = (start + end)//2
      if x == A[m]:
         return True
      elif x > A[m]:
         start = m + 1
      elif x < A[m]:
         end = m - 1

for x in M_list:
   if isIn(x, A, 0, N-1):
      print(1)
   else:
      print(0)