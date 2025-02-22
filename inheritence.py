class Createaccount:
    username="llokkkesshha"
    def Createaccount(self):
        print("acc created")
class Deleteaccount(Createaccount):
    def deleteid(self):
        print("account is deleted")
        
d=Deleteaccount()
d.deleteid()
print(d.username)


