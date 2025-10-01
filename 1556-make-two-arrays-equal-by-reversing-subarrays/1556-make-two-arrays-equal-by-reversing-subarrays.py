from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target_c=dict(Counter(target))
        arr_c=dict(Counter(arr))
        for i in target_c:
            if i in arr_c:
                if arr_c[i]==target_c[i]:
                    continue
                else:
                    return False
                    
            else:
                return False
        return True        
                