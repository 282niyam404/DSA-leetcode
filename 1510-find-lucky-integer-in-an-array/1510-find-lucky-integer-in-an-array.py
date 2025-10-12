class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_c=dict(Counter(arr))
        m=0
        for i,j in arr_c.items():
            if i==j:
                m=max(m,i)
        if m==0:
            return -1        
                
        return m
                
                