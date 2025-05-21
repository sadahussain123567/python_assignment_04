# 1 Using self
class Student:
  def __init__(self,Name,Marks):
      self.Name=Name
      self.Marks=Marks
  def display(self):
    print(f"Name:{self.Name} Marks{self.Marks}")
    
studentt=Student("Sadam Hussain","840")
studentt.display()  

# 2. Using cls
class count:
  counter =0
  def __init__(self):
    count.counter +=1
  @classmethod  
  def clss(cls):
    print(f"Count is {cls.counter}")
    
neww=count()
neww=count()
neww=count()
count.clss()

# 3. Public Variables and Methods
class Car:
  def __init__(self, Brand):
      self.Brand=Brand
      
  def Start(self):
    print(f"{self.Brand} is starting")
    
if __name__=="__main__":
 mycar=Car("Toyota")
print(f"{mycar.Brand}")  
mycar.Start()  
  
# 4. Class Variables and Class Methods

class Bank:
  bank_name="Habib bank"
  
  @classmethod
  def change_bank_name (cls,Name):
      cls.bank_name=Name
      
if __name__ == "__main__":
    user1=Bank()
    user2=Bank()
    print(f"Before changing bank name")
    print(f"Bank Name:{user1.bank_name}")
    print(f"Bank Name:{user2.bank_name}")
    
    print(f"After changing bank name")

    Bank.change_bank_name("Allied Bank")
    print(f"Bank Name:{user2.bank_name}")
    
# 5. Static Variables and Static Methods
class MathUtils:
  @staticmethod
  def add(a,b):
    return a+b
if __name__=="__main__":
  users=MathUtils.add(3,4)
  print(f"Sum:{users}")

# 6. Constructors and Destructors
class logger:
  def __init__(self):
    print("Object is created ")
  def __del__(self):
    print("Object is destroyed ")
    
log=logger()

del log


# 7. Access Modifiers: Public, Private, and Protected

class Employee:
  def __init__(self,name,salary,ssn):
    self.name=name
    self._salary=salary
    self.__ssn=ssn
    
if __name__=="__main__":    
  user1=Employee("Saddam",200000,2333)
  print(user1.name)
  print(user1._salary)
try: 
  print(user1.__ssn)
except AttributeError:
  print("Cannot access private variables")

# inheritance in python
# inheritance example
# Single Inheritance
class Caaar:
  def __init__(self,Company,Register):
    self.Company=Company
    self.Register=Register
    
  def opening(self):
      print("1909")
class model(Caaar):
   def done(self):
     return self.opening
   
user33333=model("Toyota","In Pakistan")
print(user33333.Register)

# Multi-level Inheritance

class companyyyy:
  name="Efu Life"
class Offices:
   Branches=["Hyd","Karachi","Islamabad","Lahore"]
class Regional(companyyyy,Offices):
   Hyd="Auto Bhan road"
    
resuuult=Regional()
print(resuuult.Branches[2])