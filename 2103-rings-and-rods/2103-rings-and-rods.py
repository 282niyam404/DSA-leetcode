class Solution:
    def countPoints(self, rings: str) -> int:
        nums=[i for i in rings if i.isnumeric()]
        rin=[i for i in rings if i.isalpha()]
        r={}
        for k,v in list(zip(nums,rin)):
            r.setdefault(k,[]).append(v)
        c=0
        for i in r.values():
            if len(set(i))==3:
                c+=1
            else:
                continue    
        return c