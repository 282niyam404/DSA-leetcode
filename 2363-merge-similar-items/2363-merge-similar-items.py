class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        res={}
        for k,v in items1+items2:
            if k not in res:
                res[k]=[v]
            else:
                res[k].append(v)
        for k,val in res.items():
            res[k]=sum(val)
        sorted_list = [[k, v] for k, v in sorted(res.items())]
        return sorted_list    
        