class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vov=list("aeiouAEIOU")
        split=int(len(s)/2)
        s_split_1=s[:split]
        s_split_2=s[split:]
        count_vov_1=0
        count_vov_2=0
        for i in s_split_1:
            if i in vov:
                count_vov_1+=1
        for i in s_split_2:
            if i in vov:
                count_vov_2+=1
        return count_vov_1==count_vov_2        
        