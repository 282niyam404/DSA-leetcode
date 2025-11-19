class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        g=[-i for i in gifts]
        heapq.heapify(g)
        for i in range(k):
            x=-heapq.heappop(g)
            heapq.heappush(g,-int(x**0.5))
        return -sum(g)