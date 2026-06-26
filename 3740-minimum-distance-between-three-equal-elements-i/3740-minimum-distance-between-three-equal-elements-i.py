class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        g={}
        for i,v in enumerate(nums):
            g.setdefault(v,[]).append(i)
        minn=float('inf')
    
          
        for i,v in g.items():
            if len(v)>=3:
                for i in range(len(v)-2):
                    minn = min(minn, 2 * (v[i+2] - v[i]))
            else:
                continue
        return minn if minn != float('inf') else -1       
