#libFracMix.py

class FracMix(Fraccion):

	def __init__(self,ent,num=0,den=1):
		self.ent=ent
		super().__init__(num,ent)
		self.simplifica()
		super().simplifica()

	def __str__(self):
		return str(self.ent) + super().__str__()

	def simplifica(self):
		if self.num > self.den:
			aux=self.num//self.den
			self.ent=self.ent+aux
			self.num-=(aux*self.den)

	def toFraccion(self):
		n,d = self.num,self.den
		if self.ent !=0:
			n = (self.ent * d) + n
		f = Fraccion(n,d)
		return f