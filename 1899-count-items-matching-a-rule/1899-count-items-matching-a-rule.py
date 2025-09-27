class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        
        type_d=[]
        color=[]
        company=[]
        for i in range(len(items)):
            for j in range(len(items[i])):
                if j==0:
                    type_d.append(items[i][j])
                elif j==1:
                    color.append(items[i][j])
                elif j==2:
                    company.append(items[i][j])

        dic={"type":type_d,"color":color,"name":company}
        c=0
        for i in dic[ruleKey]:
            if i==ruleValue:
                c=c+1            
        return c