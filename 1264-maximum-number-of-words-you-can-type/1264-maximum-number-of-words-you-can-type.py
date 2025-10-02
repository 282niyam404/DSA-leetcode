class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_s=text.split()
        c=0
        for i in text_s:
            for j in brokenLetters:
                if j in i:
                    c=c+1
                    break
        return len(text_s)-c            
        