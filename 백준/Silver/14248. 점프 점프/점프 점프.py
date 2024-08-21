from collections import deque

n = int(input())
m = list(map(int,input().split()))
s = int(input())-1

def solution(n,m,s):
	visited = [False] * n

	dfs(n,m,s,visited)

	return sum(visited)

def dfs(n,m,s,visited):
	visited[s] = True
	jump = m[s]

	left = s - jump
	if 0 <= left < n and not visited[left]:
		dfs(n,m,left,visited)

	right = s + jump
	if 0 <= right < n and not visited[right]:
		dfs(n,m,right,visited)

print(solution(n,m,s))


