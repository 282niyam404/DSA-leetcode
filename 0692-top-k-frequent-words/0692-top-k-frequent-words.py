class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic_f=dict(Counter(words))
        hp=[]
        for a,f in dic_f.items():
            heapq.heappush(hp,(-f,a))
        l=[]
        for i in range(len(hp)):
            f,a=heapq.heappop(hp)
            l.append(a)    
        return l[:k]