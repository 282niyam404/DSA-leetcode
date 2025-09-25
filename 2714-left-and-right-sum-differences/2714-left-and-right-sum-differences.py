class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        #left sum
        s=0
        l_sum_list=[0]
        for n in range(1,len(nums)):
            s += nums[n-1]
            l_sum_list.append(int(s))

        #right sum
        s_r=0
        r_sum_list=[0]
        for n in range(len(nums)-2,-1,-1):
            s_r += nums[n+1]
            r_sum_list.append(int(s_r))

        r_sum_list.reverse()
        #final list
        final_l=[]
        j=0
        for i in range(len(l_sum_list)):
            while j==i:
                final_l.append(abs(l_sum_list[i]-r_sum_list[j]))
                j+=1
        return final_l        

        