class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a_g=[0]
        for i in gain:
            a_g.append(a_g[-1]+i)

        return max(a_g)    
        