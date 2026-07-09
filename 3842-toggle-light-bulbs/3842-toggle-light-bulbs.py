class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        sett=set()
        for i in bulbs:
            if i not in sett:
                sett.add(i)
            else:
                sett.remove(i)
        return sorted(list(sett))        
               
        