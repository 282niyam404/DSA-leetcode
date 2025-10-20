class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        s=[]
        for i in mat:
            s.append(i.count(1))
        dic={}
        for i,x in enumerate(s):
            dic[i]=x   
        hp=[]
        for ro,st in dic.items():
            heapq.heappush(hp,(st,ro))     
        f=[]
        for _ in range(k):
            f.append(heapq.heappop(hp)[1])
        return f        
        