class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat_list=list(pattern)
        s_list=s.split()
        if len(set(s_list))!=len(set(pat_list)) or len(s_list)!=len(pat_list):
            return False
        else:    
            
            final_d=dict(zip(pat_list,s_list))
            j=0
            for i in range(len(pattern)):
                while j==i:
                    if final_d[pat_list[i]]==s_list[j]:
                        j=j+1
                        continue
                        
                    else:
                        return False
                        break
            return True
            
                        
        