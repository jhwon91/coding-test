import heapq

def solution(operations):
    # 최소 힙과 최대 힙 초기화
    min_heap = []
    max_heap = []
    # 유효한 요소를 추적하는 집합
    entry_finder = set()
    
    for operation in operations:
        if operation.startswith("I "):
            num = int(operation.split()[1])
            # 최소 힙과 최대 힙에 요소 추가
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            # 요소를 유효한 집합에 추가
            entry_finder.add(num)
        elif operation == "D 1":
            # 최대 힙에서 유효하지 않은 요소를 제거
            while max_heap and -max_heap[0] not in entry_finder:
                heapq.heappop(max_heap)
            if max_heap:
                # 최댓값 제거
                max_val = -heapq.heappop(max_heap)
                entry_finder.remove(max_val)
        elif operation == "D -1":
            # 최소 힙에서 유효하지 않은 요소를 제거
            while min_heap and min_heap[0] not in entry_finder:
                heapq.heappop(min_heap)
            if min_heap:
                # 최솟값 제거
                min_val = heapq.heappop(min_heap)
                entry_finder.remove(min_val)
    
    # 명령 처리 후 유효하지 않은 요소 제거
    while min_heap and min_heap[0] not in entry_finder:
        heapq.heappop(min_heap)
    while max_heap and -max_heap[0] not in entry_finder:
        heapq.heappop(max_heap)
    
    if not entry_finder:
        return [0, 0]
    
    min_val = min_heap[0] if min_heap else 0
    max_val = -max_heap[0] if max_heap else 0
    
    return [max_val, min_val]

