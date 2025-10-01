class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vovel="aeiou"
        co=0
        mod_words=words[left:right+1]
        for i in mod_words:
            if i[0] in vovel and i[-1] in vovel:
                print(i)
                co=co+1
            else:
                continue
        return co        
        