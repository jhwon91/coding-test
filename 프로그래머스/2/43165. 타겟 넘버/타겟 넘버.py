def solution(numbers, target):
    answer = 0
    global t ,num
    t = target
    num = numbers
    
    return dfs(0,0)

def dfs(index,CNum):
    if index == len(num):
        return 1 if CNum == t else 0
    
    add_case = dfs(index + 1, CNum + num[index])
    sub_case = dfs(index + 1, CNum - num[index])
    
    return add_case + sub_case
    