class MySet(object):
    myset_struct=[]
    
    def add(self,val):
        if(not self.myset_struct.__contains__(val)):
            self.myset_struct.append(val)
           
    def rem(self,val):
        self.myset_struct.remove(val)
    
    def union(self ,values):
        newList=self.myset_struct;
        for v in values.myset_struct:
            newList.append(v)
        return newList    

    def intersection(self,values):
        newList=[]
        for y in values.myset_struct:
            if(self.myset_struct.__contains__(y)):
                newList.append(y)
        return newList
    
    def diff(self,values):
        newList=[]
        for y in values:
            if(not self.myset_struct.__contains__(y)):
                newList.append(y)
        return newList
    def __str__(self):
        return  str(self.myset_struct)
    

mySet=MySet()
for a in range(0,100):
    mySet.add(a)
    

mySet2=MySet()
for a in range(100,200):
    mySet2.add(a)

print(mySet.union(mySet2))
  