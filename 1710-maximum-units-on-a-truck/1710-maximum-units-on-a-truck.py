class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        arr=boxTypes
        arr.sort(key=lambda x: x[1], reverse=True)
        s=0
        t_size = truckSize
        for i in arr:
            take = min(t_size, i[0])
            s += take * i[1]
            t_size -= take
            if truckSize == 0:
                break

        return s
        