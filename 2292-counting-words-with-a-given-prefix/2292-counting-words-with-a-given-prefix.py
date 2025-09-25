class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        new_words=[w[:len(pref)] for w in words]
        c=0
        for i in range(len(new_words)):
            if new_words[i]==pref:
                c+=1
        return c        
                