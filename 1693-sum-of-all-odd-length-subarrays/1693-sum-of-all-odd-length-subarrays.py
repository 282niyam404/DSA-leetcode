class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        odd_len=[i for i in range(1,len(arr)+1) if i%2!=0]
        s=[]
        for win in odd_len:
            for i in range(len(arr)-win+1):
                win_sum=sum(arr[i:i+win])
                s.append(win_sum)
        return sum(s)        

        