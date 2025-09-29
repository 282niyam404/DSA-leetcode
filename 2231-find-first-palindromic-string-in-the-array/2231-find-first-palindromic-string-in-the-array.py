class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        rev_word=[]
        for i in words:
            rev_word.append(i[::-1])
        final_dic=dict(zip(words,rev_word))   
        for key,value in final_dic.items():
            if key==value:
                return key
                break
            else:
                continue 
        return ""    
        