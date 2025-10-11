class MyHashSet:

    def __init__(self):
        self.sett=set()
        

    def add(self, key: int) -> None:
        if key not in self.sett:
            self.sett.add(key)
        
        

    def remove(self, key: int) -> None:
        if key in self.sett:
            self.sett.discard(key)
        

    def contains(self, key: int) -> bool:
        if key in self.sett:
            return True
        else:
            return False    
        


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(4)
obj.remove(7)
param_3 = obj.contains(4)