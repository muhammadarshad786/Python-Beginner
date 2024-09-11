print('hello')
name='arshad'
print(23+23)
age=23
secondage=23
print(age+age)
print(type(name))

b=True
aa=None
# punctutors operator
# (),{},#,@,-=,+=,/=,=,*=
# languages    types of languages
# implicit jo inder sy find krti hai or type nhi btano parta hai  , explicit is to types btana parta hai

# expression exectution
a,b=2,3
text='@'
print(2*text*3)   #jab number or sting sath ati hai int first and 6 time repeate string
#concatination of string into string
aaaa='areshad'
bbb='ali'
print((aaaa+bbb)*b)


# expression percedince  boarmas rule
number=3
number1=3
number2=4
print(number+number1*number2)

# arithmetic express come with integer and float result in float

number3=8.9
number4=3
print(number3+number4)
#  division may float may answer aye ga
print(number3/number4)

# integer division  //  come with float or int ,int will gine but display float
print(number3//number4)  # is same as the floor choose the closest number 2.3 tu 2  and -4.8  tu -5

# denominatoi is negative answer in negative   symbole    %   
number5=9.0
number6=-3.3
print(number5%number6)


# taking input from user 

name=input('name :')  # for the string type
agee=int(input('age: '))  # for the integar 
floatage=float(input('float :'))



# conditional statement

light=input('Enter light:')

if(light=='red'):
    print('stop')
elif(light=='green'):
    print('go')
elif(light=='yellow'):
    print('Ready to ')
else:
    print('light broken')
    
    
    
# single line if else or ternary operator

sweet=input('Enter Sweet :')

eat= 'apple' if sweet=='apple' else 'no'


# clever if ternary operator

# <value>=('yes','no') [condition]

sal=input('Enter salary')

salary=('yes','no') [sal>10000]




# conversion 
# one is type conversion python interparetor automatic convert it 
# second is type cast jo khud forcefuly krwaty hai

version=float('6.6')
good=7
print(version+good)   # this is type casting

version1=7.008
version2=7
print(version1+version2)   # this is type conversion


# indexing 

harshlikare='rapper'
print(harshlikare[5])
print(len(harshlikare))  #lenght of string



# slicing index : accessing a parts of string  mean string to turdna parts krna
# varibale[starindex:endindex]   start wala include to ta hai end wala nhi
print(harshlikare[0:4])

# negative index be krskty hai    -1 sy start

# string function
study='i am studying python'
print(study.endswith('on'))   # it return true and false

print(study.capitalize())   #original string ky under change nhi krta hai ik bar kam krta hai

print(study.replace('am','you'))  
print(study.find('am'))    #index return krta hai  first jo aye ga am bad may koi hai tu woh ignor hai
print(study.count('am'))  #yeh word kitne bar repeat ho va hai  


# Find Even and odd Number

Even=int(input('Enter Number: '))

if(Even%2==0):
    print('Its Even Number')
else:
    print('odd Number')
