class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        remainder = len(s) % k
        if remainder != 0:
            s = s + fill * (k - remainder)
        li=[]
        start=0
        end=k
        while start<=len(s)-k:
            li.append(s[start:end])
            start=end
            end+=k
        return li    
