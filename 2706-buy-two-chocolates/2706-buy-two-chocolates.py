class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices_sort=sorted(prices)
        win_size=2
        for i in range(len(prices_sort)-win_size+1):
            if sum(prices_sort[i:i+win_size])>money:
                return money
                break
            else:
                return money-sum(prices_sort[i:i+win_size])
                break
        
        