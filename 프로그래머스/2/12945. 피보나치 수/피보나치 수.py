# 재귀로 풀었으나 시간 복잡도에서 막힘
# def solution(n):
#     answer = 0
    
#     def fibo(number):
#         if number == 0:
#             return 0
#         elif number == 1:
#             return 1
#         else:
#             return fibo(number-1) + fibo(number-2)
        
#     answer = fibo(n) % 1234567
        
#     return answer


def solution(n):
    answer = 0
    dp = [0,1]
    
    if n > 1:
        for num in range(2,n+1):
            dp.append(dp[num-1] + dp[num-2])
    
    answer = dp[n] % 1234567
        
    return answer