class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        g={}
        for u,v in edges:
            g.setdefault(u,[]).append(v)
            g.setdefault(v,[])
        k = list(range(n))   
        v=[]    
        
        for i in g.values():
            v.extend(i)
        x=set(k)-set(v)
        if len(x)!=1:
            return -1
        else:
            return list(x)[0]       
        