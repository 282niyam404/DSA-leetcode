class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        li=[]
        com=[]
        for i in range(1,n+1):
            if li==target:
                break
            li.append(i)
            com.append("Push")
            if i not in target:
                com.append("Pop")
                li.pop()   
        return com           
        