import pygame
import random
screen = pygame.display.set_mode([640,480])
allrects = {}
class Grob():
	def __init__(self,x,y,health,speed,state):
		self.x 			= x
		self.y			= y
		self. health 	= health
		self.speed	 	= speed
		self.state 		= state
		self.state 		= ["running","top"]
	def move(self):
		self.speed *= 1.0002
		self.rect = pygame.Rect(self.x,self.y,12,10)
		if self.state[0] == "running":
			for i in allrects:
				i2 = allrects.get(i)
				i2[0] -= self.speed
				print (i2)
		##keyboard
		k = pygame.key.get_pressed()
		if k[pygame.K_SPACE]:
			self.state[1] = "top"
		elif not k[pygame.K_SPACE]:
			self.state[1] = "bot"

		if self.state[1] == "top":
			if self.y != 32:
				self.y -= self.speed*4
			if self.y < 32:
				self.y = 32
		if self.state[1] == "bot":
			if self.y != 448:
				self.y += self.speed*4
			if self.y > 448:
				self.y = 448

	def col(self):
		for i in allrects:
			if self.rect.colliderect(allrects.get(i)):
				self.speed = 1
class Block():
	def __init__(self,x,y,w,h,rectname):
		self.x 			= x
		self.y			= y
		self.w			= w
		self.h 			= h
		self.rect 		= None
		self.rectname 	= rectname
		self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
	def draw(self):

		if self.rectname not in allrects:
			allrects[self.rectname] = self.rect
			self.rect = allrects.get(self.rectname)

		pygame.draw.rect(screen,[255,120,33],self.rect)
	def random(self):
		if self.rect[0] < -40:
			self.rect[0] = 1000
			
			self.rect[1] = random.choice([0,64])
			if self.rect[1] == 0:
				self.rect[3] = random.randint(60,416)
			if self.rect[1] == 64:
				self.rect[3] = 480
