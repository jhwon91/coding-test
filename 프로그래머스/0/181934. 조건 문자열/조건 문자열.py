def solution(ineq, eq, n, m):
    answer = 0
    if ineq == ">" and eq == "=":
        if n >= m:
            return 1
        return 0
    elif ineq == ">" and eq == "!":
        if n > m:
            return 1
        return 0
    elif ineq == "<" and eq == "=":
        if n <= m:
            return 1
        return 0
    elif ineq == "<" and eq == "!":
        if n < m:
            return 1
        return 0
    