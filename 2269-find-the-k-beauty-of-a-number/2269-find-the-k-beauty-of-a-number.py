class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_l = str(num)
        c=0
        for i in range(len(num_l)-k+1):
            sub=num_l[i:i+k]
            divd=int("".join(sub))
            if divd==00:
                continue
            if num%divd==0:
                c+=1
        return c        
        