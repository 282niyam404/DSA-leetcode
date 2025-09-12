class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk=[]
        for i in operations:
            if i=="+":
                #do this
                su=int(stk[-1])+int(stk[-2])
                stk.append(su)


            elif i=="D":
                #do this
                last_ele=stk[-1]
                stk.append(2*int(last_ele))
            elif i=="C":
                #do this
                stk.pop()
            else:
                #do this
                stk.append(int(i)) 
        return sum(stk)              
