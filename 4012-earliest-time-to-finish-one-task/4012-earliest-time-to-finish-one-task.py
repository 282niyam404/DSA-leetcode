class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        
        m=sum(tasks[0])
        for i in tasks:
            m=min(m,sum(i))
        return m    
                