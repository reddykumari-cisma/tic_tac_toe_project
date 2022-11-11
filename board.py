import numpy
class board
m_array
def __init__(self)
 self.m_array=numpy.array([[[occupancyType.empty,occupancyType.empty,occcupancyType.empty],[occupancyType.empty,occupancyType.empty,occupancyType.empty],[occupancyType.empty,occupancyType.empty,occupancyType.empty]]])
def getBoard(self)
 return self.m_array
def setBoard(self,arr)
 self.m_array=arr
def printInfo(self)
 print("print all the object info:",self.m_array)
def getPosition(self,x,y)
 if x>=0 and x<3:
     if y>=0 and y<3:
         return self.m_array[x][y]
def setPosition(self,x,y,occupancyType)
 if x>=0 and x<3:
     if y>=0 and y<3:
         self.m_array[x][y]=occupancyType
         return true
     else
        return false
    else
       return false
def initialize(self)
 for i in range(3)
  for j in range(3)
   self.m_array[i][j]=occupancyType.empty

def prettyPrint(self)
 return self.m_array
