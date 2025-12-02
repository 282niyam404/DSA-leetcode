class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        li=[]
        for i in strs:
            if i.isnumeric():
                li.append(int(i,10))
            else:
                li.append(len(i))
        return max(li)        
        
        