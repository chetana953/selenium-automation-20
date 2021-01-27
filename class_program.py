class ABC:
    def display(self):
        print('hello we are in class')
    def addition(self):
        a=10
        b=20
        print(a+b)

obj=ABC()
obj1=ABC()
obj2=ABC()

obj.display()
obj1.display()
obj2.display()
obj.addition()

class XYZ:
    age=30
    def _init_(self,address,rollno):
        self.name='sqltools'
        self.add=address
        self.roll=rollno
        self.show_data(8000)
    def show_data(self,salary):
        print(f'name:{self.name},age:{XYZ.age},salary:{salary}')
        print(f'address:{self.add},roll no:{self.roll}')
    def greeting(self):
        print('hello good morning')

