def solution1(word):
    answer = 0
    
    weights = [781, 156, 31, 6, 1]  # [625+125+25+5+1, 125+25+5+1, 25+5+1, 5+1, 1]
    
    dic = {
        'A': 0,
        'E': 1,
        'I': 2,
        'O': 3,
        'U': 4
    }
    
    for w in range(len(word)):
        answer += dic[word[w]] * weights[w] + 1
    
    return answer

def solution2(word):
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


if __name__ == "__main__":
	import time
	import datetime

	start = time.time()
	word = 'UUU'
	print(solution2(word))
	sec = time.time() - start

	times = str(datetime.timedelta(seconds=sec))
	short = times.split('.')[0]
	print(f"{times} sec")
	print(f"{short} sec")