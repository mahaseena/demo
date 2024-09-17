class person:
    def __init__(self, name , id):
        self.name=name
        self.id =id

    def display(self):
        print(self.name,  self.id)
class emp1(person):
    #constructor chaining
    def __init__(self, name, id,sal, des):
        super().__init__(name, id)
        self.sal=sal
        self.des=des

    def show(self):
        #method chaining
        super().display()
        print(self.sal,self.des)

p1=person('mass',101)
p1.display()
e1=emp1('rohith',102,40000,'dev')
e1.show()
print('hello')