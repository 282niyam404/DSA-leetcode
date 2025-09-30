class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1=list(set(nums1)-set(nums2))
        num2=list(set(nums2)-set(nums1))
        fin=[]
        fin.append(num1)
        fin.append(num2)
        return fin
        