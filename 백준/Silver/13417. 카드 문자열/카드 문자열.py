import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def solution(n, data):
	answer = []
	answer.append(data[0])
	
	q = deque(data[1:])
	
	while q:
		alphabet = q.popleft()

		if ord(alphabet) <= ord(answer[0]):
			answer.insert(0,alphabet)
		else:
			answer.append(alphabet)

	return ''.join(answer)

for _ in range(T):
	N = int(input())
	DATA = list(input().split())
	print(solution(N,DATA))

