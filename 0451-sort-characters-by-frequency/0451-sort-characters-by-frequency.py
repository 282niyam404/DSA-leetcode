class Solution:
    def frequencySort(self, s: str) -> str:
        dic=dict(Counter(s))
        hep=[]
        for alp,freq in dic.items():
            heapq.heappush(hep,(-freq,alp))
        r=""
        while hep:
            f, a = heapq.heappop(hep)
            r += a * (-f)
        return r      
        