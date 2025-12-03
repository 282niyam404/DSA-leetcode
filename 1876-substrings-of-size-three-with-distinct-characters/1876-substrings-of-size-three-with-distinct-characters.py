class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        win_size=3
        dist_count=0
        for i in range(len(s)-win_size+1):
            if len(set(s[i:i+win_size]))==3:
                dist_count+=1
            else:
                continue
        return dist_count        
        