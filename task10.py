class MySet(object):
    
    def __init__(self):
          self.myset_struct=[]
    
    def add(self,val):
        if(not self.myset_struct.__contains__(val)):
            self.myset_struct.append(val)
           
    def rem(self,val):
        self.myset_struct.remove(val)
    
    def union(self ,values):
        res = MySet()
        res.myset_struct=self.myset_struct.copy()
        for v in values.myset_struct:
            res.add(v)
        res.myset_struct.sort();
        return res

    def intersection(self,values):
        res=MySet();
        for y in values.myset_struct:
            if(self.myset_struct.__contains__(y)):
                res.add(y)
        res.myset_struct.sort()            
        return res
    
    def diff(self,values):
        res=MySet();
        for y in values.myset_struct:
            if(not self.myset_struct.__contains__(y)):
                res.add(y)
        res.myset_struct.sort()  
           
        return res
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




print("set1 and set 2 diff",mySet.diff(l))
print("set1 and set 2 intersection",mySet.intersection(l))
print("set1 and set 2 union",mySet.union(l))
print("set1 and set 2 intersection",mySet.intersection(l))
  