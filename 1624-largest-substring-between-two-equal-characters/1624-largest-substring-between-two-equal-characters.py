class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic={}
        for i,v in enumerate(s):
            dic.setdefault(v,[]).append(i)
        li=[]
        for key , val in dic.items():
            if len(val)>=2:
                li.append(val)  
        if len(li)==0:
            return -1
        else:              
            dist=0
            for i in li:
                dist=max(dist,(max(i)-1)-min(i))      
            return dist    
              
        