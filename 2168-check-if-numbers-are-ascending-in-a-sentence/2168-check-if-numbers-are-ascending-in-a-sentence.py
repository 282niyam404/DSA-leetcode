from collections import Counter
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        x=s.split()
        nums_s=[]
        for i in x:
            if i.isalpha():
                continue
            else:
                nums_s.append(int(i))
        
        count_d=dict(Counter(nums_s))
        count_d
        for i in count_d:
            if count_d[i]>1:
                return False
        return nums_s==sorted(nums_s)             
                