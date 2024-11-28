class UndergroundSystem:
    def __init__(self):
        self.customer = {}
        self.time = {}
    
    # Solution for Variant
    # def time_to_minutes(self, time_str):
    #     hours, minutes = map(int, time_str.split(':'))
    #     return hours * 60 + minutes

    def checkIn(self, id: int, startStation: str, checkinTime: int) -> None:
        self.customer[id] = (startStation, checkinTime)
        # self.customer[id] = (startStation, self.time_to_minutes(checkinTime))
        
    def checkOut(self, id: int, endStation: str, checkoutTime: int) -> None:
        startStation, checkinTime = self.customer[id]
        # checkoutTimeInMinutes = self.time_to_minutes(checkoutTime)
        route = (startStation, endStation)

        if route not in self.time:
            self.time[route] = [0, 0] # [total_time, count]
        self.time[route][0] += checkoutTime - checkinTime
        # self.time[route][0] += checkoutTimeInMinutes - checkinTime
        self.time[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.time[(startStation, endStation)]
        return total / count


    # Vaiant: When the time is in a clock format: 9: 30

    # TC: O(1)
    # SC: O(N + R) - N is the number of unique customers and R is the unique number of routes


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
