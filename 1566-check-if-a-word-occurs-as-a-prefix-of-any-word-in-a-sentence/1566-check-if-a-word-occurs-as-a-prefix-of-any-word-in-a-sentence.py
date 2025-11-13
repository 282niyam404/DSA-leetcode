class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        x=sentence.split()
        for i in range(len(x)):
            if len(x[i])>=len(searchWord):
                if searchWord==x[i][:len(searchWord)]:
                    return i+1
        return -1            

        