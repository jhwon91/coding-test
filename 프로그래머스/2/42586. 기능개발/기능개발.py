from collections import deque

def solution(progresses, speeds):
	answer = []
	d = deque(progresses)
	while d:
		for i in range(len(d)):
			d[i] += speeds[i]
		
		count = 0

		if d[0] >= 100:
			for i in range(len(d)):
				if d[0] >= 100:
					d.popleft()
					del speeds[0]
					count += 1
				else:
					break
		if count > 0:
			answer.append(count)
	return answer
