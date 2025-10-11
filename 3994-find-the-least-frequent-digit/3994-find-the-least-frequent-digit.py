class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        num = list(str(n))
        fin=dict(Counter(num))
        min_freq = min(fin.values())
        least = [int(d) for d, c in fin.items() if c == min_freq]
        if least==[]:
            return []
        else:    
            return min(least)
        