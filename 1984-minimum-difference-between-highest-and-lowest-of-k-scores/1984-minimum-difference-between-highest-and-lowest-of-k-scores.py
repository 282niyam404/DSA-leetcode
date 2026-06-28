class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums_sort=sorted(nums)
        minn=max(nums_sort)
        win_size=k
        for i in range(len(nums_sort)-win_size+1):
            minn=min(minn,max(nums_sort[i:i+win_size])-min(nums_sort[i:i+win_size]))
        return minn