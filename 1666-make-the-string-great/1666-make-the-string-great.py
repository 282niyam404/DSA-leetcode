class Solution:
    def makeGood(self, s: str) -> str:
        stac = []
        for i in s:
            stac.append(i)
            if len(stac) > 1:
                if (ord(stac[-2]) - ord(stac[-1]) == 32) or (ord(stac[-2]) - ord(stac[-1]) == -32):
                    stac.pop()
                    stac.pop()
        return "".join(stac)
         
                