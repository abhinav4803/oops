class car:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
# you pass arugment (brand,model) when creating the object and __init set them instance varible
  def display(self):
    print("car Brand:",self.brand,"car.model:", self.model)
car1=car("ford","endavour")
car1.display()
    