class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=s.lower()
        final_l=""
        for i in x:
            if i.isalnum():
                final_l+=i
            else:
                continue
        r=0
        l=len(final_l)-1
        while r < l:  
            if final_l[r] != final_l[l]:
                return False
            r += 1
            l -= 1
        return True        
                