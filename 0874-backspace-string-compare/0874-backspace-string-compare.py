class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk_s=[]
        stk_t=[]
        for i in s:
            if i != "#":
                stk_s.append(i)
                 
            else:
                if stk_s:
                    stk_s.pop()
        for j in t:
            if j != "#":
                stk_t.append(j)
            else:
                 if stk_t:
                    stk_t.pop()
        return stk_s==stk_t        
                