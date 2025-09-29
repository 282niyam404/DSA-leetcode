class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
        first_let=[]
        if len(words)==len(s):
            for i in words:
                first_let.append(i[0])
            return "".join(first_let)==s
        else:
            return False        