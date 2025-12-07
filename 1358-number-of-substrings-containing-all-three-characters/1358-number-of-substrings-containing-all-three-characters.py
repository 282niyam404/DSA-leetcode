class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = {'a': -1, 'b': -1, 'c': -1}
        ans = 0
        
        for i, ch in enumerate(s):
            if ch in last:
                last[ch] = i
            
            
            if -1 not in last.values():
                ans += min(last.values()) + 1

        return ans