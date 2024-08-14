def solution(keymap, targets):
    answer = [0] * len(targets)
    
    temp = dict()
    for key in keymap:
        for idx,k in enumerate(key):
            if k in temp:
                temp[k] = min(temp[k],idx+1)
            else:
                temp[k] = idx + 1
    
    print(temp)
    
    for idx,tar in enumerate(targets):
        
        for t in tar:
            if t in temp:
                answer[idx] += temp[t]
            else:
                answer[idx] = -1
                break
    return answer