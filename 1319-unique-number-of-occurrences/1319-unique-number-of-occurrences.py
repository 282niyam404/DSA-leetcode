from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ar_count=dict(Counter(arr))
        s=set()
        for val in ar_count.values():
            if val not in s:
                s.add(val)
            else:
                return False
        return True             
        
        