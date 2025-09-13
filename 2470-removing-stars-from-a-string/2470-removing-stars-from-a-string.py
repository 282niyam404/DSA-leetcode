class Solution:
    def removeStars(self, s: str) -> str:
        stk=[]
        for i in s:
            if i != "*":
                stk.append(i)
            elif i=="*":
                stk.pop()
        return "".join(stk)             

        