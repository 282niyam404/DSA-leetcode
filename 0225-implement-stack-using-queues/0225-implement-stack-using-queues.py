from collections import deque
class MyStack:

    def __init__(self):
        self.my_que=deque()
        

    def push(self, x: int) -> None:
        
        self.my_que.append(x)
        

    def pop(self) -> int:
        if self.my_que:
            return self.my_que.pop()
        

    def top(self) -> int:
        if self.my_que:
            return self.my_que[-1]
        

    def empty(self) -> bool:
        return len(self.my_que) == 0   
        


#Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(5)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()