class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        co=0
        x=set(allowed)
        for i in range(len(words)):
            if set(words[i])-x==set() :
                co=co+1
        return co        
        