class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dic={}
        for i ,v in enumerate(s):
            dic.setdefault(v,[]).append(i)
        for ch, pos in dic.items():
            dist = pos[1] - pos[0] - 1

            if dist != distance[ord(ch) - ord('a')]:
                return False

        return True          
        