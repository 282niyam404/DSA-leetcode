class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c=0
        s=coins
        for i in costs:
            if i<=s:
                c+=1
                s=s-i
            else:
                break    
        return c    
               
        