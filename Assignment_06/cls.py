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