def solution(word):
    answer = 0
    word_arr = []
    def create_word(c_word):
        if len(c_word) <= 5:
            word_arr.append(c_word)
            for i in ['A', 'E', 'I', 'O', 'U']:
                create_word(c_word+i)
    
    create_word('')
    
    answer = word_arr.index(word)
    return answer