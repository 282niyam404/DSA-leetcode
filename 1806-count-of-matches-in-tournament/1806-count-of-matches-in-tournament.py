class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches_played = []
        teams_advanced = []
        i = 0

        while n>1:
            matches_played.append(n // 2)           
            teams_advanced.append(n - (n // 2))    
            n = teams_advanced[-1]
        return sum(matches_played)    
           



        