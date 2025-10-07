class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dict_c=dict(Counter(arr))
        ap=[]
        for i in dict_c:
            if dict_c[i]==1:
                ap.append(i)
        if len(ap)>=k:        
            for i in range(len(ap)+1):
                if i==k:
                    return ap[k-1]       
        return ""