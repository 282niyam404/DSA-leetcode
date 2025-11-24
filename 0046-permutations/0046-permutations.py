class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        x=list(permutations(nums,len(nums)))
        fin=[]
        for i in x:
            x=list(i)
            fin.append(x)
        return fin    
                   

        