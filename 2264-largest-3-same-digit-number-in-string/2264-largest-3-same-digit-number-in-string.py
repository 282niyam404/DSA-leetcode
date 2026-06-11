class Solution:
    def largestGoodInteger(self, num: str) -> str:
        win_size=3
        sett=set()
        for i in range(len(num)-win_size+1):
            n=num[i:win_size+i]
            if len(set(n))==1:
                if n not in sett:
                    sett.add(n)
            else:
                continue
        if sett:
            return max(sett)
        return ""    