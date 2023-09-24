class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()
        self.counter = 0

    def consec(self, num: int) -> bool:
        self.queue.appendleft(num)

        if self.queue[0] == self.value:
            self.counter += 1
        else:
            self.counter = 0

        if self.counter >= self.k:
            return True
        return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
