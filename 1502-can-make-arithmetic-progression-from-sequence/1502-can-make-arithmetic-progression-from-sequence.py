class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff=arr[1]-arr[0]
        win_size=2
        for i in range(len(arr)-win_size+1):
            st=arr[i:i+win_size]
            if st[-1]-st[-2]==diff:
                continue
            else:
                return False
                break
        return True 
        