class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li=[]
        for x in nums1:
            idx=nums2.index(x)
            for y in nums2[idx:]:
                if y>x:
                    li.append(y)
                    break
            else:
                li.append(-1)       
        return li        
        