class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # 시작점에 장애물이 있는 경우, 경로는 0입니다.
        if obstacleGrid[0][0] == 1:
            return 0
        
        # dp 배열을 0으로 초기화합니다.
        dp = [[0] * n for _ in range(m)]
        
        # 시작 위치를 1로 설정합니다.
        dp[0][0] = 1
        
        # 첫 번째 열을 채웁니다.
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
        
        # 첫 번째 행을 채웁니다.
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
        
        # 나머지 dp 테이블을 채웁니다.
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # 결과는 dp 테이블의 오른쪽 아래에 있습니다.
        return dp[-1][-1]

# 사용 예시:
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0],[0,0,0]]
solution = Solution()
area = solution.uniquePathsWithObstacles(obstacleGrid)
print(area)
