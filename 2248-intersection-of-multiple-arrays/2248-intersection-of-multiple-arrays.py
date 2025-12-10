class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        dic=[]
        for i in nums:
            dic.append(dict(Counter(i)))
        common = set(dic[0].keys())

        for mp in dic[1:]:
            common = common.intersection(mp.keys())

        ans = sorted(list(common))
        return ans
        