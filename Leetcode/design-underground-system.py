class UndergroundSystem:
    def __init__(self):
        self.customer = {}
        self.time = {}

    def checkIn(self, id: int, startStation: str, checkinTime: int) -> None:
        self.customer[id] = (startStation, checkinTime)
        

    def checkOut(self, id: int, endStation: str, checkoutTime: int) -> None:
        startStation, checkinTime = self.customer[id]
        route = (startStation, endStation)
        if route not in self.time:
            self.time[route] = [0, 0]
        self.time[route][0] += checkoutTime - checkinTime
        self.time[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.time[(startStation, endStation)]
        return total / count
        
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
