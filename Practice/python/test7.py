class Solution(object):
    def calcEquation(self, equations, values, queries):
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            
            visited.add(start)
            
            for neighbor in graph[start]:
                if neighbor in visited:
                    continue
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return result * graph[start][neighbor]
            
            return -1.0
        
        # 그래프 생성
        graph = {}
        
        for (a, b), value in zip(equations, values):
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = value
            graph[b][a] = 1 / value
        
        # 쿼리에 대한 결과 계산
        result = []
        for a, b in queries:
            if a in graph and b in graph:
                result.append(dfs(a, b, set()))
            else:
                result.append(-1.0)
        
        return result

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

solution = Solution()
max_area = solution.calcEquation(equations,values,queries)
print(max_area)