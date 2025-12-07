class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        fin={}
        for u,v in logs:
            if u not in fin:
                fin[u]=[v]
            else:
                if v not in fin[u]:
                    fin[u].append(v)        
        a = [0] * k

        for us in fin:
            con = len(fin[us])      
            a[con - 1] += 1

        return a   

        