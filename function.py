def show(n):
    print(n)
show(3)

# recresive function
# def showdata(g):
#     if(g==0):
    
#         return
#     else:
#         print(g)
#         show(g-1)   
# showdata(5)
# call stack  funciton ki call and stack create krta hai


def fact(n):
    if(n==0):
        return 
    print(n )
    fact(n-1)
fact(3)


def recresive(n):
    print('hello')
    if(n==0 or n==1):
        return 1
    else:
        return n * recresive(n-1)
print(recresive(4))


# list of fruits

def list_fruits(listfr ,inx=0):
    if(inx==len(listfr)):
        return 
    
    print(listfr[inx])
    list_fruits(listfr,inx+1)
        
fruits=['banana','apple','mango']
list_fruits(fruits)