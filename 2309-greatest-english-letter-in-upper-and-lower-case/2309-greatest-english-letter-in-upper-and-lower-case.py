class Solution:
    def greatestLetter(self, s: str) -> str:
        
        sett = set(s)

        for ch in range(ord('Z'), ord('A') - 1, -1):
            if chr(ch) in sett and chr(ch + 32) in sett:
                return chr(ch)

        return ""        
        