class Solution:
    def countAsterisks(self, s: str) -> int:
        stk=""
        count=0
        for i in s:
            if i=='|':
                count+=1
            if count%2==0:
                stk+=i
        count_ash=0
        for i in stk:
            if i=="*":
                count_ash+=1
        return count_ash                


        