class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        best = (-1, -1)  

        for i, r in enumerate(mat):
            cnt = r.count(1)
            if cnt > best[1]:
                best = (i, cnt)

        return list(best)     
        