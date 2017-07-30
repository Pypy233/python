class Birds:
	def _init_(self):
		self.hungry = True
	def eat(self):
		if self.hungry:
			print("I'm hungry!")
			self.hungry = False
		else:
			print("No, thanks!")

class SongBirds(Birds):
	def _init_(self):
		super(SongBirds, self)._init_()
		self.sound = 'Squawk!'
	def sing(self):
		print(self.sound)

b = Birds()
b._init_()
b.eat()

sb = SongBirds()
sb._init_()
sb.sing()

