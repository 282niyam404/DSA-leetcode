class Solution:
    def makeFancyString(self, s: str) -> str:
        stk=[]
        for i in s:
            stk.append(i)
            if len(stk)>=3:
                if stk[-1]==stk[-2]==stk[-3]:
                    stk.pop()
                    continue
                else:
                    continue
        return "".join(stk)           
        