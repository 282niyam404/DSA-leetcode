class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        win_size=3
        final=[]
        for i in range(len(mountain)-win_size+1):
            arr=mountain[i:win_size+i]
            if arr[1]>arr[0] and arr[1]>arr[2]:
                final.append(i+1)  
        return final        
        