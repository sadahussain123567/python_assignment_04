# 1 Using self

class Student:
  def __init__(self,Name,Marks):
      self.Name=Name
      self.Marks=Marks
  def display(self):
    print(f"Name:{self.Name} Marks{self.Marks}")
    
studentt=Student("Sadam Hussain","840")
studentt.display()  