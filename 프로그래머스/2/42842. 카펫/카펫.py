# 카펫의 넚이 = width * height = brown + yellow
# yellow = (width - 2) * (height - 2)
def solution(brown, yellow):
    S = brown + yellow
    
    for height in range(3, S + 1):
        width = S//height
        if (width - 2) * (height - 2) == yellow:
            return [width, height]
        
