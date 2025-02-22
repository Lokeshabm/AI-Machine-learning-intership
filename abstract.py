from abc import ABC  , abstractmethod
class CreateAccount(ABC):
    @abstractmethod
    def create(self):
        pass
class DeleteAccount(CreateAccount):
    def create(self):
        print("deleteAccount")
    def sample(self):
        print("from sample mothod")
           
obj=DeleteAccount()
print(obj.create())
print(obj.sample())


class Car(ABC):
    @abstractmethod
    def we(self):
        pass
class BMW(Car):
    def we(self):
        print('4')
    def amount(self):
        print("2,00,00,000")
    def seats(self):
        print("4 seats")


obj2=BMW()
print(obj2.we())
print(obj2.amount())
print(obj2.seats())