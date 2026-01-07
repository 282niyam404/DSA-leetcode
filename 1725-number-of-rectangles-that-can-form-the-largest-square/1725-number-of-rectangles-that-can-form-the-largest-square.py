class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        l=[]
        for i in rectangles:
            l.append(min(i))
        maxx=Counter(l)
        maxx_side=max(maxx.keys())
        return maxx[maxx_side]    
        