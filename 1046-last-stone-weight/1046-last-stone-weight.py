class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s=[-i for i in stones]
        heapq.heapify(s)
        while len(s)>1:
            x=-heapq.heappop(s)
            y=-heapq.heappop(s)
            if x!=y:
                heapq.heappush(s,-(x-y))
        if s:
            return -s[0]
        else:
            return 0
        