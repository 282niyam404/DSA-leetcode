from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s_dict=dict(Counter(s))
        return len(set(s_dict.values()))==1
        