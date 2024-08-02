def solution(citations):
    answer = 0
    
    citations.sort(reverse = True) #내림차순 정렬
    
    for idx, citation in enumerate(citations):
        if idx + 1 <= citation:
            answer = idx + 1
    
    return answer