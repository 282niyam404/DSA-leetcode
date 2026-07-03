class Solution:
    def findValidPair(self, s: str) -> str:
        s_count = Counter(s)

        for i in range(len(s) - 1):
            sub = s[i:i+2]

            if sub[0] == sub[1]:
                continue

            valid = True
            for ch in sub:
                if s_count[ch] != int(ch):
                    valid = False
                    break

            if valid:
                return sub

        return ""