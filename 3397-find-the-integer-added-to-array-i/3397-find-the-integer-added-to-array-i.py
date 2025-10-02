class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        if sum(nums2)<sum(nums1):
            return int((sum(nums2)-sum(nums1))/len(nums1))
            
        else:
            
            return int(abs((sum(nums1)-sum(nums2))/len(nums1)))