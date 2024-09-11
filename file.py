f=open('demo.txt','r')
data=f.read()
print(data)
print(type(data))
# for reading specfice character
# data=f.read(3) index pass krty hai 0 to three read kr na hai
# f.readline()
f.close()

filessss=open('demo.txt','w')
filessss.write('hello im a software engineer')
filessss.close()
filo=open("demo.txt","a+")
filo.write("\nhelo im a ")
filo.close()

# as   alias mean hota hai same function and access it with f

with open("demo.txt","w") as f:
    data=f.write('im in wayout lab')
    
with open("sample.txt","r") as f:
    data=f.read()
new_data=data.replace('testing',"deploying")
print(new_data)

with open("sample.txt","w") as f:
    data=f.write("hello im testing the file write mode")
    print(data)
    
word='testing'
with open("sample.txt","r") as f:
    data=f.read()
    if(data.find(word) !=-1 ):
        print('Data Will Be found')
    else:
        print("Not Found")
        
        
        
def check_line_no():
    word='testing'
    line_no=0
    conditions=True
    with open("sample.txt","r") as f:
        
        while conditions:
            
            conditions=f.readlines()
            print(conditions)
            if(word in conditions):
                print(line_no)
                return
            else:    
              line_no += 1
    print("not foud")
    return -1
check_line_no()    