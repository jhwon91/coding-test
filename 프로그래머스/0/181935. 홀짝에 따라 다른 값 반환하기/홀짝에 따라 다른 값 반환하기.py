def solution(n):
    answer = 0
    for x in range(n+1):
        if x % 2 == 0 and n % 2 == 0:
            answer += (x**2)
        elif x % 2 == 1 and n % 2 == 1:
            answer += x
    return answer