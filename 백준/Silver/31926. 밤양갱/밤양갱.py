import sys
input = sys.stdin.readline

N = int(input())
daldidalgo = 8
daldidan = 2
count = 0
while N>1:
	N //= 2
	count += 1

print(daldidalgo + count + daldidan)