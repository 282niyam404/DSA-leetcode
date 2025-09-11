class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        len_nums=len(nums)
        set_nums=set(nums)
        set_actual=set(i for i in range(1,len_nums+1))
        return list(set_actual-set_nums)
         
        