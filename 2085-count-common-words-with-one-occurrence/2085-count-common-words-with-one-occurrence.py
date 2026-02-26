class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1=Counter(words1)
        c2=Counter(words2)
        sett_1=set()
        sett_2=set()
        for k,v in c1.items():
            if v>1:
                continue
            else:
                sett_1.add(k)
        for k,v in c2.items():
            if v>1:
                continue
            else:
                sett_2.add(k)      
        return len(sett_1 & sett_2)          
        