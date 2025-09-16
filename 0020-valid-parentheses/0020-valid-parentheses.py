class Solution:
    def isValid(self, s: str) -> bool:
        para_map={"(":")","[":"]","{":"}"}
        stk=[]
        for i in s:
            if i in para_map:
                stk.append(i)
            else:
                if not stk or para_map[stk[-1]]!=i:
                    return False

                stk.pop()
                    
        return not stk
    
        