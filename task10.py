class MySet(object):
    
    def __init__(self):
          self.myset_struct=[]
    
    def add(self,val):
        if(not self.myset_struct.__contains__(val)):
            self.myset_struct.append(val)
           
    def rem(self,val):
        self.myset_struct.remove(val)
    
    def union(self ,values):
        for v in values.myset_struct:
            self.add(v)
        self.myset_struct.sort()
        return self.myset_struct  

    def intersection(self,values):
        for y in values.myset_struct:
            if(self.myset_struct.__contains__(y)):
                self.add(y)
        self.myset_struct.sort()  
        print(self.myset_struct)        
        return self.myset_struct
    
    def diff(self,values):
        newList=[]
        for y in values.myset_struct:
            if(not self.myset_struct.__contains__(y)):
                newList.append(y)
        newList.sort()
        self.myset_struct=newList;         
        return newList
    def __str__(self):
        return  str(self.myset_struct)
    
  
mySet=MySet()
for a in range(1,15,3):
    mySet.add(a)
    

print(" set1 ",mySet)
l=MySet()
for a in range(3,10):
    l.add(a)

print("set2 ",l)




print("set1 and set 2 union",mySet.union(l))
print(mySet.myset_struct)
print("set1 and set 2 diff",mySet.diff(l))
print("set1 and set 2 intersection",mySet.intersection(l))
  