import heapq

def solution(scoville, K):

    heapq.heapify(scoville)
    
    repeat_count = 0
    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        if first >= K:
            return repeat_count
        
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        repeat_count += 1

    return repeat_count if scoville[0] >= K else -1


result = solution(
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    0
)

print(result)