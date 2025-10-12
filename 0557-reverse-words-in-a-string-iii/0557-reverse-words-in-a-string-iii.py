class Solution:
    def reverseWords(self, s: str) -> str:
        f=[]
        x=s.split()
        for i in x:
            f.append(i[::-1])
        return " ".join(f)    
        