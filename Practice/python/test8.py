class Solution(object):
    def findRightInterval(self, intervals):
        # 구간의 시작점과 해당 구간의 인덱스를 저장합니다.
        starts = []
        for i, interval in enumerate(intervals):
            starts.append((interval[0], i))
        
        # 시작점 기준으로 정렬합니다.
        starts.sort()
        
        result = []
        for interval in intervals:
            end = interval[1]
            min_index = -1
            min_start = float('inf')
            
            # 직접 오른쪽 구간을 찾습니다.
            for start, index in starts:
                if start >= end and start < min_start:
                    min_start = start
                    min_index = index
            
            result.append(min_index)
        
        return result
intervals = [[3,4],[2,3],[1,2]]
solution = Solution()
max_area = solution.findRightInterval(intervals)
print(max_area)