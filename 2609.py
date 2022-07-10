import sys

a, b = map(int, sys.stdin.readline().split())
a1, b1 = a, b

if a < b:
    a, b = b, a
while(b != 0):
    remain = a % b
    a = b
    b = remain

gcf = a
lcm = (a1 * b1) // gcf
print(gcf)
print(lcm)
