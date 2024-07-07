def solution(s, skip, index):
    answer = ''
    pre = []
    for i in range(ord("a"),ord("z")+1):
        if skip.find(chr(i)) > -1:
            continue
        pre.append(chr(i)) 
        
    for i in s:
        
        if pre.index(i) + index >= len(pre):
            print(pre.index(i) + index)
            print(len(pre))
            print(pre)
            nextIndex = (pre.index(i) + index) % len(pre)
        else:
            nextIndex = pre.index(i) + index
        answer += pre[nextIndex]
    
    return answer