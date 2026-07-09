class Solution:
    def countMonobit(self, n: int) -> int:
        dic={}
        for i in range(n+1):
            dic[i]=bin(i)[2:]
        c=0
        for v in dic.values():
            if len(set(v))==1:
                c+=1
        return c        