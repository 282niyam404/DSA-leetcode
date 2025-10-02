class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        co=0
        for i in range(len(words)):
            if set(words[i])-set(allowed)==set() :
                co=co+1
        return co        
        