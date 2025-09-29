class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        nums = str(num)
        rev_1=int(nums[::-1])
        rev_2=int(str(rev_1)[::-1])
        return rev_2==num
        if nums=="0":
            return True
        elif str(rev_1)[0]=="0":
            return False    

        