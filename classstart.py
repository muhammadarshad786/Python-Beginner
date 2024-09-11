class Student:     #class is a blueprint and object is an instance of blueprint
    name='arshad'
student1=Student()  #here we create the object 

del student1

# print(student1.name)

# constructure of class
# __init__() is and init function or constructure
# onject creation time per invoke hota hai

class Teacher:
    # default constructure 
    def __init__(self):  
        pass 
    # paramaterized constructure
    def __init__(self,fullname):   #self parameter is a reference of the instance
        self.name=fullname
        print('constructure are call automatic')
t1=Teacher('Arshad')

print(t1)   #print the location and it is an object
print(t1.name)

del t1



# attribute are the data are store example variable are store data and date are store in variable in ko hum attributes kehty hai


# class Attributes and instance Attributes

# class Atributes are those varible are created once and it occopyed once and it same 
# instance attributes are define in constructure


# exapmle three student are from same university theire name and roll no are different but class and university name
# are same

class University:
    university_name='ABC University'
    def __init__(self,rollno,name):   #if the class attributes are same with instance attributes 
        self.name=name                #  instance attributes priority are greater than class attriutes
        self.rollno=rollno
    def wellcome(self):
        print('wellcome to our team') 
    def Data(self):
        print(self.name,self.rollno)
        print('wellcome to our team')   
        
    @staticmethod      #static methods are those that changes the behavoir of the method
    def hello():
        pass
# how to access attributes
uni1=University(102022,'Arshad')
# instance attributes
print(uni1.rollno,uni1.name)

# class attributes
print(University.university_name)

uni1.wellcome()
uni1.Data()

del uni1

