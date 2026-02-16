class Solution:
    def similarPairs(self, words: List[str]) -> int:
        co=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if set(words[i])==set(words[j]):
                    co+=1
                else:
                    continue
        return co            
        