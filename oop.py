
# abstraction   #encapsulation  #inheritance #polymorphism

# abstraction are hide unnecessary thing from user and show necessary things to user
# for exapmle car and driver ,driver does not know about engine and fuils how they works
# only enjoy driving 

class Car:
    def __init__(self):
        self.accelator=False
        self.brk=False
        self.clutch=False
    
    def start(self):
        self.accelator=True
        self.clutch=True
        print('Car Start')
        
car1=Car()
car1.start()
del car1

# encapsulation are have data and function are wrapped into single instance

# Private Attributes and methods

class Privatesss:
    __Pin=222
    def __init__(self,name,password):
        self.name=name
        self.pasword=password
    def _SayHello(self):
        print(self.__Pin)
        print('Hello World')
    def Wellcome(self):
        self._SayHello()
        
pri1=Privatesss('Arshad',70122919)
pri1.Wellcome()