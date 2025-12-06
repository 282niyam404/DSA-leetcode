class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"

        while len(s) < k:
            temp = ""
            for ch in s:
                nxt = chr(ord(ch) + 1)
                if nxt > 'z':                   
                    nxt = 'a'
                temp += nxt
            s += temp

        return s[k-1]
        