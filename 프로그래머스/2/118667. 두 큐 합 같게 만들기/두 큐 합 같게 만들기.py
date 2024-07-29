# 두 큐 합 같게 만들기

from collections import deque

def solution(queue1, queue2):
    answer = 0
    sum1 = sum(queue1) # 큐1의 합
    sum2 = sum(queue2)
    total = sum1 + sum2
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    while total // 2 != sum1:
        if sum1 > sum2:
            
            q1_pop = q1.popleft() # 맨 앞 원소 제거
            sum1 -= q1_pop 
            q2.append(q1_pop)
            sum2 += q1_pop	

        else:
            q2_pop = q2.popleft()
            sum2 -= q2_pop
            q1.append(q2_pop)
            sum1 += q2_pop
        answer += 1
        
        if (len(q1) + len(q2)) * 2 < answer:
            return -1
    return answer