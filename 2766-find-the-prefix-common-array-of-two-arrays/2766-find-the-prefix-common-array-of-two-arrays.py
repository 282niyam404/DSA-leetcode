class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:    
        win_size=1
        li=[]
        i=0

        for j in range(len(A)-win_size+1):
            s_a=A[0:j+win_size]
            s_b=B[0:j+win_size]
            co=set(s_a)&set(s_b)
                    
            li.insert(i,len(co))
            i=i+1 
        return li        
        