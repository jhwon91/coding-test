
found_primes = set()

def solution(numbers):
    answer = 0
    
    visited = [0] * len(numbers)
    dfs("",numbers,visited)
    answer = len(found_primes)
    return answer

def dfs(currntN,numbers, visited):

    for i in range(len(numbers)):
        if visited[i] == 0:
            visited[i] =1
            tempN = currntN + numbers[i]
            
            if int(tempN) > 1 and checkNumber(int(tempN)) and int(tempN) not in found_primes:
                found_primes.add(int(tempN))

            dfs(tempN,numbers,visited)
            visited[i] =0
            

def checkNumber(N):
    for i in range(2,int(N**0.5)+1):
        if N % i == 0:
            return False
    return True
        
        