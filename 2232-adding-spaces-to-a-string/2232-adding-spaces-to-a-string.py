class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        li=[]
        for i in range(len(spaces)):
            if i==0:
                li.append(s[:spaces[i]])
            else:
                li.append(s[spaces[i-1]:spaces[i]])
        li.append(s[spaces[-1]:])
        return " ".join(li)      
        