def allowed():
    print("you are allowed")
def notallowed():
    print("you are not allowed") 
    
age=int(input("enter age"))      
g=input("enter gander")
m='male'
if(g==m and age>18):
    allowed()
else:
    notallowed()
    
