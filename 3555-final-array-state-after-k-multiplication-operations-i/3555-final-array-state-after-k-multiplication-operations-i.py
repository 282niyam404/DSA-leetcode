class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(h)

        for _ in range(k):
            val, idx = heapq.heappop(h)
            val *= multiplier
            nums[idx] = val
            heapq.heappush(h, (val, idx))
        return nums

        