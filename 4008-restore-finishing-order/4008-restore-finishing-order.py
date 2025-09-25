class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        final_l=[]
        for i in order:
            if i in friends:
                final_l.append(i)
            else:
                continue
        return final_l        
        