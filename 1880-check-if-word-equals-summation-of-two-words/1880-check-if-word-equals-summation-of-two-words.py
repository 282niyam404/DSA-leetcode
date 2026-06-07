class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        num=[i for i in range(0,26)]
        alp=list("abcdefghijklmnopqrstuvwxyz")
        dic=dict(zip(alp,num))
        fir=""
        for i in firstWord:
            fir+=(str(dic[i]))
        sec=""
        for i in secondWord:
            sec+=str(dic[i])    
        tar=""
        for i in targetWord:
            tar+=str(dic[i])    
        return int(fir)+int(sec)==int(tar)    
        