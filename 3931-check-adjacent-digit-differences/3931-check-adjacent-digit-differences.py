class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        win_size=2
        for i in range(len(s)-win_size+1):
            w=s[i:win_size+i]
            di=abs(int(w[0])-int(w[-1]))
            if di>2:
                return False
                break
        return True        
        