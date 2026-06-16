class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        x=set()
        win_size=2
        for i in range(len(s)-win_size+1):
            x.add(s[i:i+win_size])
        rv_s=s[::-1]
        c=0
        for i in x:
            if i in rv_s:
                return True
            else:
                continue   
        return False         
        