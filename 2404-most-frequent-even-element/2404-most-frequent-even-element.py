class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = Counter(nums)
        even = {k: v for k, v in count.items() if k % 2 == 0}

        if not even:
            return -1

        mx = max(even.values())
        return min(k for k, v in even.items() if v == mx)
