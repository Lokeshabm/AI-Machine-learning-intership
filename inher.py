class Create:
    def profile(self):
        print("This is ur porofile")
class Delete(Create):
    def profile(self):
        print("profile is deleted")
        
        
obj=Delete()
print(obj.profile())



class Father:
    def status(self):
         print("This is my property")
class Son(Father):
    def status(self):
        print("This my father's property")
        
       
obj=Son()
print(obj.status())




