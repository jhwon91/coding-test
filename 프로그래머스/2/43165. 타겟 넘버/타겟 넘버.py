def solution(numbers, target):
    
    def dfs(index, total):
        if len(numbers) == index:
            if total == target:
                return 1
            else:
                return 0
        
        return dfs(index+1, total - numbers[index]) + dfs(index+1, total + numbers[index])
    
    return dfs(0,0)


    