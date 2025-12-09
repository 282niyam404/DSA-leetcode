class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score_t=[]
        for i in score:
            score_t.append(tuple(i))
        score_t_sort=sorted(score_t,key=lambda x:x[k],reverse=True)
        final=[list(i) for i in score_t_sort]
        return final    
        