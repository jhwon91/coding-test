import sys
input = sys.stdin.readline
# 재귀 깊이 설정
sys.setrecursionlimit(10**6)
n = int(input())
dices = [list(map(int,input().split())) for _ in range(n)]

opposite = {
	0:5,
	1:3,
	2:4,
	3:1,
	4:2,
	5:0
}

def searchMaxValue(dice,bottom, top):
		sideValues = [i for i in dice if i != bottom and i != top]
		return max(sideValues)


def dfs(diceIdx, bottomValue):
	if diceIdx == n:
		return 0
	
	dice = dices[diceIdx]

	bottomIndex = dice.index(bottomValue)
	topIndex = opposite[bottomIndex]

	currentTopValue = dice[topIndex]
	currentBottomValue = bottomValue

	maxSide = searchMaxValue(dice,currentTopValue,currentBottomValue)

	return maxSide + dfs(diceIdx+1, currentTopValue)

maxSum = 0
for bottomValue in range(1,7):

	maxSum = max(maxSum, dfs(0, bottomValue))

print(maxSum)