class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        g={}
        for u,v in paths:
            g.setdefault(u,[]).append(v)
            g.setdefault(v,[])
        for source in g.keys():
            if [source] in g.values() and g[source]==[]:
                return source    
                