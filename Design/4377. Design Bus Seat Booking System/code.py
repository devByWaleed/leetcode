from typing import List

class BusBooking:

    def __init__(self, n: int):
        self.system = []
        self.map = {
            "A": 1, "B": 2,
            "C": 3, "D": 4
        }
        
        for i in range(n):
            self.system.append([])
            for j in range(1, 5):
                self.system[i].append(False)
        

    def toggle(self, seat: str) -> None:
        row_num = int(seat[1:])
        total_time = 0

        if seat[0] == "B" or seat[0] == "C":
            if not self.system[row_num][self.map[seat[0]]]:
                total_time += 1
        else:
            if not adjacent_seat_checking:
                total_time += 1
            else:
                total_time += 3
        

    def getTotalTime(self) -> int:
        pass
        

    def getMinTime(self) -> int:
        pass
        


# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()

obj = BusBooking()
print(obj.__init__(["BusBooking","toggle","toggle","getTotalTime","getMinTime","toggle","toggle","getTotalTime","getMinTime"]))
print(obj.__init__([[20],["B3"],["A3"],[],[],["C3"],["D3"],[],[]]))
print(obj.__init__(["BusBooking","toggle","toggle","getTotalTime","toggle","toggle","toggle","getTotalTime","getMinTime"]))
print(obj.__init__([[10],["C7"],["D7"],[],["D7"],["C7"],["D7"],[],[]]))

# T.C:  O()
# S.C:  O()
