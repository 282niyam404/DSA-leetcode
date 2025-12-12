class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        li=[]
        for i in range(1,numRows+1):
            li.append(i*[1])
        final=[]
        win_size=2
        for i in range(len(li)):
            mid=[]
            if len(li[i])<=2:
                final.append(li[i])
            else:
                for i in range(len(final[-1])-win_size+1):
                    mid.append(sum(final[-1][i:i+win_size]))
                final.append([1]+mid+[1])    
        return final