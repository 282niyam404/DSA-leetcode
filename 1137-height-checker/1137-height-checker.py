class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        h_s=sorted(heights)
        j=0
        co=0
        for i in range(len(heights)):
            while j==i:
                if heights[i]==h_s[j]:
                    j=j+1
                    continue
                else:  
                    co+=1
                    j=j+1
        return co            
        