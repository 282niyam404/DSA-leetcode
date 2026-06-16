class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        p=(5/100)*len(arr)
        i=0
        left=0
        while i!=p:
            arr.pop(left)
            arr.pop()
            i+=1
        mean = sum(arr) / len(arr)
        return mean
        