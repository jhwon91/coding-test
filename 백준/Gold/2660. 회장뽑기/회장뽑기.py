import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
data = []

# 친구 관계 입력 처리 (-1 -1로 종료)
while True:
	temp = list(map(int,input().split()))
	if temp[0] == -1:
		break	
	data.append(temp)

graph = [[] for _ in range(N+1)]
for i,j in data:
	graph[i].append(j)
	graph[j].append(i)

# BFS를 통해 특정 회원의 점수를 계산하는 함수
def bfs(start):
	maxCount = 0 # 해당 회원의 최대 거리 (점수)
	visited = [False] * (N+1)
	q = deque([(start,0)])
	visited[start] = True

	while q:
		currentNode, currentCount = q.popleft()

		for nextNode in graph[currentNode]:
			if not visited[nextNode]:
				visited[nextNode] = True
				q.append((nextNode,currentCount+1))
				maxCount = max(maxCount,currentCount+1)
	return maxCount


# 각 회원의 점수를 저장할 배열
candidate = [0] * (N+1)


# 모든 회원에 대해 BFS 실행하여 점수 계산
for i in range(1,N+1):
	candidate[i] = bfs(i)


# 최소 점수 찾기
resultNum = min(candidate[1:])


# 최소 점수를 가진 회원(회장 후보) 찾기
resultArr = list(filter(lambda x:candidate[x] == resultNum, range(len(candidate))))


# 결과 출력
print(resultNum, len(resultArr))
print(' '.join(map(str,resultArr)))

