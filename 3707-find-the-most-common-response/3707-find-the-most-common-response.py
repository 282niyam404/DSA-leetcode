class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        final=[]
        for i in responses:
            s=set(i)
            for j in s:
                final.append(j)
        f_c=Counter(final)
        words=[]
        max_it=max([i for i in f_c.values()])
        for word,co in f_c.items():
            if co==max_it:
                words.append(word) 
        words.sort()        
        return words[0]       
        