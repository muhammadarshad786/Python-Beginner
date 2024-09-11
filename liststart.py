Marks=[34,45,567,23,23]  # list ky under hum string ,float int store kra skty hau

print(len(Marks))
print(Marks[0])

student=['ali',56,90.0]

print(student) 
# string is immutable jo changes nhi krskty thy us ky index ki value ko
#list is mutable

print(student[0])
student[0]='raza'
print(student)

# slicing
print(student[0:4])

# list methods
# append are add value at last
# sort is ascending order 
# sort  is decending
# reverse 
# insert

listofstudent=['ali','raza','arshad','ali']
print(listofstudent.append('good'))
print(listofstudent.sort())
print(listofstudent.sort(reverse=True))
print(listofstudent.insert(0,'pinki ponki'))
print(listofstudent.reverse())  #yeh reverse orignal string may krta hai
# print(listofstudent.insert(0,'pinki ponki'))

listofstudent.remove('ali')   # value delete krta hai jo phely ati hai
listofstudent.pop(1)


# tuple is immutable is similar like array 

tup=(7,)
print(type(tup))
tup1=(1,5,8,9,50,9)
print(tup1.index(9)) #return index
print(tup1.count(9)) #count total occurance


dict={
    'name':['arshad','ali'],
    'class':'2nd year',
    'project':'FYP',
     'subject':{
         'chemister',
         'physics',
         'bio',
         'math'
     }
}

print(dict.values())
print(dict.keys())
print(dict.items())
print(dict.update({'print':'hello'}))


# set are like dictories and they canot store dictories and list because they are immutable 

collection={12,3,4,5,6,7,8,8,'hello','world','hello'}  #they ignored the repeated value

coll1=set()  #yeh empthy set ko likny ka arika
# set are mutable but element are immutable  

coll1.add(1)
coll1.add(2)
coll1.add(3)
coll1.add(1)

coll1.remove(2)
coll1.clear()


print(collection.pop())

set1={1,2,3,4,5}
set2={1,2,3,4,5,6,7,8,9}
print(set1.union(set2))
print(set1.intersection(set2))





# loop in python 

i=0
while i<3:
    print('hello')
    
collectionofmovie=['killer','call','dangle']

while i<len(collectionofmovie):
    
    print('hello')
    i +=1
    
    
    
srt11=['hello','world']

for value in srt11:
    print(value)
    
    
# range function used in for loop 
#  take three first start point it optional when you not give it start from zero and second stop point
# third is step size increase number 
for val in range(2):
    print('hello')
for vsal in range(2,4,2):
    print(vsal)