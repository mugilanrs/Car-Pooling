import heapq
def Car(trips,capacity):
    trips.sort(key=lambda t: t[1])
    minHeap = []
    curPass = 0
    for t in trips:
        numpass, start, end = t
        while minHeap and minHeap[0][0] <= start:
            curPass -= minHeap[0][1]
            heapq.heappop(minHeap)

        curPass += numpass
        if curPass > capacity:
            return False
        heapq.heappush(minHeap, [end, numpass])
    return True
