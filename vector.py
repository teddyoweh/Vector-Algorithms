import math
class Vectors:
    def __init__(self) :
      pass
 
    def inputs(self,u,v):
        self.u = u
        self.v = v
        vu = u.split(',')
        self.vu =list(map(int,vu))
        vv = v.split(',')
        self.vv = list(map(int,vv))
    def Magnitude(self,u):
        vu = u.split(',')
        vu =list(map(int,vu))
        wh = (vu[0]**2)+(vu[1]**2)
        mag = math.sqrt(wh)
        return mag
    def DotProduct(self):
        
        vu = self.vu
        vv = self.vv
        ians = (vu[0]*vv[0])+(vu[1]*vv[1])
        return ians
    def  Angle(self):

        pro = self.DotProduct(self.u,self.v)
        um =  self.Magnitude(self.u)
        vm = self.Magnitude(self.v)
        vum = um*vm
        tar = pro/vum
        ans = math.acos(tar)
        return math.degrees(ans)