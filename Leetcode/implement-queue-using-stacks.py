class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.size = 0
        
    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.size += 1
        
    def pop(self) -> int:
        if self.size < 1:
            return None
        else:
            self.size -= 1
            return self.stack1.pop(0)


    def peek(self) -> int:
        if self.size < 1:
            return None
        else:
            return self.stack1[0]
        

    def empty(self) -> bool:
        if self.size == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
