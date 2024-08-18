def solution(s):
    answer = 0
    open_arry = ['[','{','(']
    close_arry = [']','}',')']
    pair = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for i in range(len(s)):
        cycle = s[i:] + s[:i]
        if cycle[0] not in open_arry:
            continue
        
        stack = [] #False
        confirm = True
        
        for c in cycle:
            if c in open_arry:
                stack.append(c)
            elif c in close_arry:
                if stack and stack[-1] == pair[c]:
                    stack.pop()
                else:
                    confirm = False
                    break
        
        if len(stack)==0 and confirm:
            answer += 1
            
    return answer