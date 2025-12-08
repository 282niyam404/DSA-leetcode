class Solution:
    def sortVowels(self, s: str) -> str:
        vav={"A","E","I","O","U","a","e","i","o","u"}
        vov_l=[ord(i) for i in s if i in vav]    
        heapq.heapify(vov_l)
        final=[]
        for i in s:
            if i in vav:
                x=heapq.heappop(vov_l)
                final.append(chr(x))
            else:
                final.append(i)
        return "".join(final)    