class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis=set()
        stk=[0]
        while stk:
            room=stk.pop()
            if room in vis:
                continue
            vis.add(room)
            for key in rooms[room]:
                stk.append(key)
        return len(vis)==len(rooms)             
        