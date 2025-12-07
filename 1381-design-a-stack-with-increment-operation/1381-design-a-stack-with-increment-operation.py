class CustomStack:

    def __init__(self, maxSize: int):
        self.stk=[]
        self.maxSize=maxSize
        

    def push(self, x: int) -> None:
        if len(self.stk)<self.maxSize:
            self.stk.append(x)
        

    def pop(self) -> int:
        if self.stk:
            return self.stk.pop()
        else:
            return -1    
            
        

    def increment(self, k: int, val: int) -> None:
        limit = min(k, len(self.stk))
        for i in range(limit):
            self.stk[i]=self.stk[i]+val
        


# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(5)
obj.push(7)
param_2 = obj.pop()
obj.increment(3,2)