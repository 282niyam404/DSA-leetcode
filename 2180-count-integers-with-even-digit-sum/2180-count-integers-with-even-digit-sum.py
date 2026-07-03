class Solution:
    def countEven(self, num: int) -> int:
        c=0
        for i in range(1,num+1):
            num=str(i)
            li=[]
            for i in num:
                li.append(int(i))
            if sum(li)%2==0:
                c+=1
            else:
                continue  
        return c        
        