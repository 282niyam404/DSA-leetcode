from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count=dict(Counter(s))
        for val in s_count:
            if s_count[val]==1:
                return(s.index(val)) 
                
            else:
                continue
        return -1  


        