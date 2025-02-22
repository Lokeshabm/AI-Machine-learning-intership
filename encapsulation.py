class Bank:
    def __init__(self,name):
        self.__name = name
        
    def getData(self):
        return self.__name
obj = Bank("abhi")

print(obj.getData())


class Createacc:
    def __init__(self,username):
        self.__username=username
    def Create(self):
        return self.__username
class Deleteacc(Createacc):
    def delete(self):
        print("acc is deleted ")
        
        
obj=Deleteacc("lokesha")
print(obj.Create())
print(obj.delete())

