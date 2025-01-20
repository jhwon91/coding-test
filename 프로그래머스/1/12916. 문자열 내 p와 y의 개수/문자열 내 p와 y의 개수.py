def solution(s):
    answer = True
    s = s.lower()
    pcount = 0
    ycount = 0
    
    for w in s:
        if w == 'p':
            pcount += 1
        elif w == 'y':
            ycount += 1
            
    if pcount != ycount:
        answer = False
        
    return answer