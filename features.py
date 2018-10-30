from enum import Enum

class Brand(Enum):
	LG = 0
	Samsung = 1
	Sony = 2

class Size(Enum):
	FortyThree = 0
	FortyNine = 1
	FiftyFive = 2

class Cost(Enum):
	Low = 0 # < 70k
	Medium = 1 # 70k - 1l
	High = 2 # 1-1.5l
	VeryHigh = 3 # 1.5l -3l
	Premium = 4 # > 3l

class Picture(Enum):
	FHD = 0
	FHDTRI = 1	
	UHD = 2 # 4K
	UHDTRI = 3 # 4K Triluminous
	
class Sound(Enum):
	W14 = 0
	W20 = 1
	W30 = 2	
	W40 = 3
	W50 = 4
	W60 = 5

class Model:
	def __init__(self,mid,modelno,size,brand,cost,picture,sound):
		self.id = mid
		self.model = modelno
		self.brand = brand
		self.size = size
		self.cost = cost
		self.picture = picture
		self.sound = sound
		self.clas = None
	def __repr__(self):
    		return "<Brand = " + str(self.brand) + "; size= " + str(self.size) + "; cost= " + str(self.cost)+"; picture= " + str(self.picture)+"; id=P" + str(self.id+1)+"; model= " + str(self.model)+"; sound= " + str(self.sound) + "; class= " + str(self.clas)+">"
	def __ne__(self, other): 
        	return self.id != other.id
	def __eq__(self, other): 
        	return self.id == other.id
	def assignClass(self, clas):
		self.clas = clas
