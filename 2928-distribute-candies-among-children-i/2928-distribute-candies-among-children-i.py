class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        co=0
        for i in range(0,limit+1):
            if i==n:
                co+=1
                break       
            for j in range(0,limit+1):
                if (i+j)==n:
                    co+=1
                    break
                for k in range(0,limit+1):
                    if (i+j+k)==n:
                        co+=1
                        break
        return co                
        