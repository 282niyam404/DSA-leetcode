class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        win_size=1
        c=0
        while win_size<=len(s):
            for i in range(len(s)-win_size+1):
                if s[i:win_size+i].count("1")<=k or s[i:win_size+i].count("0")<=k:
                    c+=1
                else:
                    continue
            win_size+=1   
        return c    
        