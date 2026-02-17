class Solution:
    def repeatedCharacter(self, s: str) -> str:
        l={}
        for i in range(len(s)):
            if s[i] not in l:
                l[s[i]]=1
            else:
                return s[i]
                break
        