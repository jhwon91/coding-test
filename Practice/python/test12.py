

def compare(i,j,s):
	if s == '>':
		return i > j
	elif s == '<':
		return i < j


def backtrack(index, num):
	if index == k + 1:
		result.append(num)
		return

	for n in range(10):
		if not visited[n]:
			if index == 0 or compare(int(num[-1]),n,symbol[index - 1]):
				visited[n] = True
				backtrack(index + 1, num + str(n))
				visited[n] = False
				
k = int(input())
symbol = input().split()
visited = [False] * 10
result = []
backtrack(0,"")
print(min(result))
print(max(result))

# 2
# < >