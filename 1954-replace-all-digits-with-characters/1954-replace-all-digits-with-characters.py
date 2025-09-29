class Solution:
    def replaceDigits(self, s: str) -> str:
        stk=[]
        for i in s:
            if i.isalpha():
                stk.append(i)
            else:
                stk.append(chr(ord(stk[-1])+int(i)))
        return "".join(stk)        

        