import itertools

def solution(babbling):
    speak = ["aya", "ye", "woo", "ma" ]
    word = []
    answer=0
    for i in range(1,len(speak)+1):
        speak_arry = list(itertools.permutations(speak, i))
        for n in speak_arry:
            word.append(''.join(n))
    
    for i in range(len(babbling)):
        for j in range(len(word)):
            if babbling[i] == word[j]:
                answer += 1
        
    return answer