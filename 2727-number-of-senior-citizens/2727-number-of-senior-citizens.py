class Solution:
    def countSeniors(self, details: List[str]) -> int:
        age_det=[d[11:13] for d in details]
        cou=0
        for i in age_det:
            if int(i)>60:
                cou+=1
        return cou        
        