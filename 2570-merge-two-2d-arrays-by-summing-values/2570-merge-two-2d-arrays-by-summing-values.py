class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        gr={}
        for u,v in nums1+nums2:
            gr.setdefault(u,[]).append(v)
            gr.setdefault(v,[])
        final_l=[]
        for i,v in gr.items():
            if v!=[]:
                final_l.append([i,sum(v)])
            else:
                continue    
        final_sorted=sorted(final_l,key=lambda x:x[0])   
        return final_sorted     
    
        