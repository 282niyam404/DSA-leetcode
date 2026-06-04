class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word_set=set(word)
        c=0
        for i in word_set:
            if chr(ord(i)+32) in word_set:
                c+=1
        return c        
        