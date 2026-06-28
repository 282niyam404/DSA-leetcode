class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        win_size=k
        li=[]
        for i in range(len(blocks)-win_size+1):
            sub=blocks[i:i+win_size]
            li.append(sub)
        c=k
        for i in li:
            c=min(c,i.count("W"))    
        return c    
        