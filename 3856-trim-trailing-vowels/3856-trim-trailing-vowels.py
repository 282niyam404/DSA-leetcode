class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vov={"a","e","i","o","u"}
        rev=list(s)
        while rev and rev[-1] in vov:
            rev.pop()
        return   "".join(rev)  
        

        