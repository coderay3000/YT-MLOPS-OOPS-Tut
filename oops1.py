# initiate a class
class employee:
    # special method /magic method/dunder method - contstructor(to define data/att)
    def __init__(self):
        print("started using att/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("att/data have been initiated") # you will see data will execute automatically but not methods

    #when we make any func inside class it called method

    def travel(self,destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")  

    
# create an obj/instance of the class
sam = employee()
#printing the  attributes
#print(sam.salary)

# calling a method
#sam.travel("Kerala")
print(type(sam))
