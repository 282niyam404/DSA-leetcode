class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        li=[i for i,v in enumerate(s) if v==c]
        finnal=[]
        for i in range(len(s)):
            dis=[abs(i-j) for j in li]
            finnal.append(min(dis))
        return finnal    
        