 

class Students:
    
    def __init__(self, m1,m2):
        
        self.m1=m1
        self.m2=m2
        
    def __add__(self,other):
        
        m1= self.m1 + other.m1
        m2= self.m2 + other.m2
        s3 = Students(m1+m2)
        
        return s3
        
    def __gt__(self,other):
        
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
       
        if r1 > r2:
           return True
        else:
            return False
    
    def __str__(self):
        
        return '{},{}'.format(self.m1,self.m2)
    
    
    
    
    
s1= Students(44,77)
s2 = Students(79,303)

if s1 > s2:
    print ("r1 wins")
else:
    print ("r2 wins")
    
print(s1. __str__() )
print(s2. __str__())




