class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        s = []
        for i in range(1, len(height)): 
            if height[i-1] > threshold:
                s.append(i)
        return s        
                

        