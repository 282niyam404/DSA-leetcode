class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        a_factor=[]
        b_factor=[]
        for i in range(1,a+1):
            if a%i==0:
                a_factor.append(i)
        for j in range(1,b+1):
            if b%j==0:
                b_factor.append(j) 
        return len(set(a_factor)&set(b_factor))