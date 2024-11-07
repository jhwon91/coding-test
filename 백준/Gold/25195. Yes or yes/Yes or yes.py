# 팬클럽 곰곰이를 만나게 된다면 "Yes"
# 팬클럽 곰곰이를 만나지 않고 이동하는 방법이 존재한다면 "yes" 

# 1에서 출발
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(M)]
panCnt = int(input())
panLocation = list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
startNode = 1
endNode = []

#단방향 그래프
for i,j in data:
	graph[i].append(j)

#BFS 초기화
q = deque([startNode])
visited[startNode] = True

# 팬이 있는곳 방문 처리
for i in panLocation:
	visited[i] = True

# end node 찾기
for i in range(1,len(graph)):
	if len(graph[i]) == 0:
		endNode.append(i)

result = 'Yes'

# 팬클럽 곰곰이가 시작 노드에 있는지 확인
if startNode in panLocation:
    print(result)
    sys.exit()

while q:
	currentNode = q.popleft()
	
	if currentNode in endNode:
		result = 'yes'
		break

	for nextNode in graph[currentNode]:
		if not visited[nextNode]:
			visited[nextNode] = True
			q.append(nextNode)

print(result)
