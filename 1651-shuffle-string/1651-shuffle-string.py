class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        final_d=dict(zip(indices,s))
        final_s=""
        for i in range(len(s)):
            final_s=final_s+final_d[i]
        return final_s    
        