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
		self.state 		= 2
		self.running	= True
	def move(self):
		self.speed *= 1.0005
		self.rect = pygame.Rect(self.x,self.y,12,10)

		if self.running :	
			for i in allrects:
				i2 = allrects.get(i)
				i2[0] -= self.speed

		##keyboard
		k = pygame.key.get_pressed()
		if k[pygame.K_UP]:
			self.state = 1
		if k[pygame.K_DOWN]:
			self.state = 2

		if self.state == 1:
			if self.y != 32:
				self.y -= self.speed*4
			if self.y < 32:
				self.y = 32
		if self.state == 2:
			if self.y != 448:
				self.y += self.speed*4
			if self.y > 448:
				self.y = 448

	def col(self):
		for i in allrects:
			if self.rect.colliderect(allrects.get(i)):
				pygame.draw.rect(screen,[255,0,0],[0,0,640,480])
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

		pygame.draw.rect(screen,[120,0,0],self.rect)

	def random(self):
		if self.rect[0] < -40:
			self.rect[0] = 1000
			
			self.rect[1] = random.choice([0,random.randint(64,416)])
			if self.rect[1] == 0:
				self.rect[3] = random.randint(60,416)
			if self.rect[1] == 64:
				self.rect[3] = 480
