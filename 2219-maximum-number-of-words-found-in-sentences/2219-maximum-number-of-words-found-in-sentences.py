class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        final_l=[]
        for i in sentences:
            final_l.append(i.split())
            c=0
        c_now=0
        for j in final_l:
            c_now=len(j)
            if c_now>c:
                c=c_now
            else:
                continue
        return c