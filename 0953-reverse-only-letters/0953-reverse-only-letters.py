class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        x = list(s)
        left = 0
        right = len(x) - 1

        while left < right:
            if x[left].isalpha() and x[right].isalpha():
                x[left], x[right] = x[right], x[left]
                left += 1
                right -= 1
            elif not x[left].isalpha():
                left += 1
            elif not x[right].isalpha():
                right -= 1

        return "".join(x)   

        
        