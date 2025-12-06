class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        alp=list("abcdefghijklmnopqrstuvwxyz")
        num=["1","2","3","4","5","6","7","8","9","10#","11#","12#","13#","14#","15#","16#","17#","18#","19#","20#","21#","22#","23#","24#","25#","26#"]
        dic=dict(zip(num,alp))
        stk = []


        for i in s:
            stk.append(i)

            if i == "#":
                
                
                fin = ''.join(stk[-3:])       
                num.append(dic[fin])
                for i in range(3):
                    stk.pop()
                stk.append(dic[fin]) 
        final_str=""
        for i in stk:
            if i.isnumeric():
                final_str+=dic[i]
            else:
                final_str+=i
        return final_str        
            
        
        