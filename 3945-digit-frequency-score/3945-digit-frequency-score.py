class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n_str=str(n)
        n_counter=Counter(n_str)
        dict(n_counter)
        summ=0
        for i ,c in n_counter.items():
            summ+=int(i)*c
        return summ    
        