class Solution:
    def balancedStringSplit(self, s: str) -> int:
        co=0
        bal=0
        for i in s:
            if i=="L":
                bal+=1
            else:
                bal-=1
            if bal==0:
                co+=1
        return co            
        