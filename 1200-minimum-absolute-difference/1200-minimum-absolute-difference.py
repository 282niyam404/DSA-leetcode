class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minn=arr[-1]-arr[0]
        for i in range(len(arr)-1):
            minn=min(minn,arr[i+1]-arr[i])
        x=[]
        win_size=2
        for i in range(len(arr)-win_size+1):
            ar=arr[i:i+win_size]
            print(ar)
            if abs(ar[-1]-ar[0])==minn:
                x.append([ar[0],ar[-1]])
        return x