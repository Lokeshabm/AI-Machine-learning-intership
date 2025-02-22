class Bike:
    color="blue"
    ger=4
    safety="zero percent"
    mylage="20 KM"
    def __init__(self,name):
        self.name = name 
    def bikeStarted(self):
        print("bike started")
    def bikestopped(self):
        print("bike is stopped")
        
b1=Bike("lokesha")
b1.bikeStarted()
print(b1.name)
print(b1.color)
print(b1.ger)
print(b1.safety)
print(b1.mylage)
b1.bikestopped()
