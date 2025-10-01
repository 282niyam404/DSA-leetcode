class Solution:
    def isBalanced(self, num: str) -> bool:
        even_s=sum([int(num[i]) for i in range(len(num)) if i%2==0])
        odd_s=sum([int(num[i]) for i in range(len(num)) if i%2!=0])
        return even_s==odd_s
        