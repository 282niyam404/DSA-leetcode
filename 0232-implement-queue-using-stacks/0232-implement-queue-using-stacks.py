from collections import deque
class MyQueue:

    def __init__(self):
        self.my_que=deque()
        
        

    def push(self, x: int) -> None:
        self.my_que.append(x)
        
        

    def pop(self) -> int:
        if self.my_que:
            return self.my_que.popleft()
        
        

    def peek(self) -> int:
        if self.my_que:
            return self.my_que[0]
        
        

    def empty(self) -> bool:
        return len(self.my_que)==0
            
        


#Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()