class Solution:
    def finalString(self, s: str) -> str:
        stk=[]
        for i in s:
            if i!="i":
                stk.append(i)
            else:
                stk.reverse()
                continue
        return "".join(stk)        
        