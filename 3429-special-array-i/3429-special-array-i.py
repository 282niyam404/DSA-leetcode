class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        bol_l=[]
        for i in nums:
            if i%2==0:
                bol_l.append(True)
            else:
                bol_l.append(False)
        win_size=2
        for i in range(len(bol_l)-win_size+1):
            f=bol_l[i:win_size+i]
            if f[0]==f[-1]:
                return False
        return True        
        