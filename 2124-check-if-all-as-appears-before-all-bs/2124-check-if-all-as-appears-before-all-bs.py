class Solution:
    def checkString(self, s: str) -> bool:
        win_size=2
        for i in range(len(s)-win_size+1):
            if s[i:win_size+i]=="ba":
                return False
            else:
                continue
        return True