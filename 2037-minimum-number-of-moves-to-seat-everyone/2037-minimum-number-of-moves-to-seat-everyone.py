class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seat_sort=[]
        student_sort=[]
        heapq.heapify(seats)
        heapq.heapify(students)
        while seats:
            seat_sort.append(heapq.heappop(seats))
        while students:
            student_sort.append(heapq.heappop(students))
        final=0
        for i in range(len(student_sort)):
            final+=abs(student_sort[i]-seat_sort[i])    
        return final    
        