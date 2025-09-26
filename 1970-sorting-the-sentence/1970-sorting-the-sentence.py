class Solution:
    def sortSentence(self, s: str) -> str:
        s_l=s.split()
        order_l=[i[-1] for i in s_l]
        fresh_l=[i[:-1] for i in s_l]
        f_d=dict(zip(order_l,fresh_l))
        final_str=""
        for i in range(1,len(fresh_l)+1):
            final_str+=f_d[str(i)]+" "
        return final_str[:-1]    
        
        