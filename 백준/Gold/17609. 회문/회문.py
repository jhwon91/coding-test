
def is_palindrome(string):
    print(get_miss_match_count(string, 0, len(string)-1, 0))
    

def get_miss_match_count(string, left, right ,count):
	if count > 1:
		return 2
	while left < right:
		if string[left] == string[right]:
			left += 1
			right -=1
		else: 
			jumpLeft = get_miss_match_count(string, left + 1, right, count + 1)
			jumpRight = get_miss_match_count(string, left, right - 1, count + 1)
			result = min(jumpLeft, jumpRight)
			return result if result <= 2 else 2
	return count


t = int(input())
for i in range(t):
    is_palindrome(input())