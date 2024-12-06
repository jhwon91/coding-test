
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
# 플로이드-워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            if data[i][k] and data[k][j]:
                data[i][j] = 1

# 결과 출력
for row in data:
    print(' '.join(map(str, row)))