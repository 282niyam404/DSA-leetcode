class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        y=[]
        for i in range(len(prices)):
            f=False
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    y.append(prices[i]-prices[j])
                    f=True
                    break
            if not f:
                y.append(prices[i])
        return y        
            
                  
           
        

        