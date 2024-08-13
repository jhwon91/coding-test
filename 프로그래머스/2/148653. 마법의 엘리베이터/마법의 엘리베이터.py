def solution(storey):
    answer = 0
    
    while storey > 0:
        current_digit = storey % 10  # 현재 자리의 숫자
        next_digit = (storey // 10) % 10  # 다음 자리의 숫자
        
        if current_digit > 5 or (current_digit == 5 and next_digit >= 5):
            # 올림 처리: 현재 자리에서 10으로 올려버림
            answer += (10 - current_digit)
            storey += 10  # 다음 자리로 올림
        else:
            # 그냥 내림 처리
            answer += current_digit
        
        storey //= 10  # 다음 자리로 이동
    
    return answer
