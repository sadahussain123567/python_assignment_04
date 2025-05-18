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
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.
class Car:
  Brand="J."
  
