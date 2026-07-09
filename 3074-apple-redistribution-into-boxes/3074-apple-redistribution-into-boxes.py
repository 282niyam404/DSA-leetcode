class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        summ_apple=sum(apple)
        cap_sort=sorted(capacity)
        c=0
        for i in cap_sort[::-1]:
            if summ_apple>0:
                summ_apple=summ_apple-i
                c+=1
        return c        
        