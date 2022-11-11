class coin
m_type
m_x_pos
m_y_pos

def __init__(self,ct)
 self.m_x_pos=-1
 self.m_y_pos=-1
 self.m_type=ct

def get_x_pos(self)
 return self.m_x_pos

def get_y_pos(self)
 return self.m_y_pos

def set_x_pos(self,x)
 self.m_x_pos=x

def set_y_pos(self,y)
 self.m_y_pos=y

def getType(self)
 return self.m_type

def setType(self,CoinType)
 self.m_type=coinType

def printInfo(self)
 print("print all the object info:",self.m_type,self.m_x_pos,self.m_y_pos)

def place(self,x,y)
 if x>=0 and x<3:
     self.m_x_pos=x
     if y>=0 and y<3:
         self.m_y_pos=y
         return true
     else
       return false
 else
   return false

def offBoard(self)
 





