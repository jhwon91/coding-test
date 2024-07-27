def solution(clothes):
    answer = 1
    temp_dict = {}
    
    for i in clothes:
        key, value = i[1],i[0]
        if key in temp_dict:
            temp_dict[key].append(value)
        else:
            temp_dict[key] = [value]

    for key in temp_dict.keys():
        if len(temp_dict) == 1 :
            return len(temp_dict[key])
        else:
            answer *= len(temp_dict[key]) + 1
    
    return answer-1