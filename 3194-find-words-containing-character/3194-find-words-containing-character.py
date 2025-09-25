class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        fin = []
        for i, word in enumerate(words):
            if x in word: 
                fin.append(i)
        return fin       


        