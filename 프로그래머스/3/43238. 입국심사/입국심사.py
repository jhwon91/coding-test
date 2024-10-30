def solution(n, times):

    start = 1
    end = max(times) * n
    answer = end

    while(start <= end):
        mid = (start + end) //2
        people = 0

        for time in times:
            people += mid // time

        if n <= people:
            answer = min(mid,answer)
            end = mid -1
        else:
            start = mid + 1
    return answer