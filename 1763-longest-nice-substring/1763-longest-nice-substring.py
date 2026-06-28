class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        win_size=2
        li=[]
        while win_size<=len(s):
            for i in range(len(s)-win_size+1):
                sub=s[i:win_size+i]
                valid = True

                for letter in sub:
                    if letter.lower() not in sub or letter.upper() not in sub:
                        valid = False
                        break

                if valid:
                    li.append(sub)

                    
            win_size+=1
        if not li:
            return ""
        return max(li,key=len)    

            