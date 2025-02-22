class Car:
    color="blue"
    no_seats=4
    def __init__(self,name):
        self.name=name
    def startAC(self):
        print("start AC")
    def startsterospeakers(self):
        print("start stero speakers")
        
        
        
class Car1:
    color="red"
    no_seats=6
    def __init__(self,name):
        self.name=name
    def startAC(self):
        print("start on AC")
    def startsterospeakers(self):
        print("start stero??// speakers")
        
       
    
car=Car("loky")
car1=Car1("bmw")
car.startAC()
car.startsterospeakers()
print(car.name)
print(car.color)
print(car.no_seats)            
car1.startAC()
car1.startsterospeakers()
print(car1.name)
print(car1.color)
print(car1.no_seats)            