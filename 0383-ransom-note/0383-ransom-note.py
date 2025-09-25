class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_count=dict(Counter(ransomNote))
        mag_count=dict(Counter(magazine))
        for x in ran_count.keys():
            if x not in mag_count or ran_count[x]>mag_count[x]:
               return False
                
            
        return True        
        