class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        grater=[i for i in nums if i>pivot]
        smaller=[i for i in nums if i<pivot]
        pivott=[i for i in nums if i==pivot]
        return smaller+pivott+grater
        
        