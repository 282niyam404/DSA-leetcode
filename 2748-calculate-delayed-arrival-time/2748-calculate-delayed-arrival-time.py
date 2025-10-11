class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        final_time=arrivalTime+delayedTime
        if final_time<24:
            return final_time
        elif final_time==24:
            return 0
        else:
            return abs(24-final_time)         
        