class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        dic={}
        for i in words:
            dic[i]=list(set(words)-set([i]))
        li=[]
        for i,v in dic.items():
            for j in v:
                if i in j:
                    li.append(i)    
        return list(set(li))            
        