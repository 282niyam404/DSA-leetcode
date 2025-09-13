class Solution:
    def removeDuplicates(self, s: str) -> str:
        sta=[]
        for i in s:
            sta.append(i)
            if len(sta)>1:
                if sta[-1]==sta[-2]:
                    sta.pop()
                    sta.pop()
        return "".join(sta)            
        