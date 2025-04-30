class student:
  def __init__(self,name,marks):
    self.name=name
    self.mark=marks
  def display(self):
    print("name",self.name,"marks",self.mark)
stu1=student("Abhinav",89)
stu2=student("singh",67)
stu1.display()
stu2.display()