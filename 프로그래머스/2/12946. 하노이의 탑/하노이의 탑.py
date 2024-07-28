def hanoi(n, from_rod, to_rod, aux_rod, moves):
    if n == 1:
        moves.append([from_rod, to_rod])
        return
    hanoi(n - 1, from_rod, aux_rod, to_rod, moves)
    moves.append([from_rod, to_rod])
    hanoi(n - 1, aux_rod, to_rod, from_rod, moves)

def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer
