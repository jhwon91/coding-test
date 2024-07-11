def solution(n, control):
    
    for spel in control:
        if spel == "w": 
            n += 1
        elif spel == "s":
            n -=1
        elif spel == "d":
            n += 10
        elif spel == "a":
            n -= 10
    
    return n