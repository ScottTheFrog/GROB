import Menu
import pygame
import random
import math
screen = pygame.display.set_mode([640,480])
allrects = {}
m = Menu.loadmenu("NOCOOKIESFORYOU.mp3")
class Grob():
	def __init__(self,x,y,health,speed,state):
		self.playerimg = pygame.image.load("grob.png")
		self.playerimg = pygame.transform.scale(self.playerimg, (32, 30))
		self.playerimg = pygame.transform.rotate(self.playerimg, 180)
		self.x 			= x
		self.y			= y
		self.health 	= health
		self.healthfont	= pygame.font.Font("freesansbold.ttf",30)
		self.speed	 	= speed
		self.state 		= state
		self.state 		= 2
		self.running	= True
		self.rotation 	= 0
		self.god		= True
		self.count		= 30
		self.meters		= 0
	def move(self):
		self.healthtxt = self.healthfont.render(str(self.health),0,[0,255,255])
		self.pointstxt = self.healthfont.render(str(round(self.meters/100)),0,[255,0,255])
		self.meters += self.speed
		screen.blit(self.healthtxt,[4,60])
		screen.blit(self.pointstxt,[4,32])
		if self.speed <= 25:
			self.speed*= 1.0005
		self.meters += self.speed

		self.rect = pygame.Rect(self.x,self.y,12,10)
		if self.rotation == 0:
			screen.blit(self.playerimg,self.rect)
		else:
			screen.blit(self.playerimg,[self.rect[0],self.rect[1]-14,self.rect[2],self.rect[3]])

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
			self.rotation = 0
			if self.y != 32:
				self.y -= self.speed*4
			if self.y < 32:
				self.playerimg = pygame.transform.rotate(self.playerimg, 180)
				self.y = 32

		if self.state == 2:
			self.rotation = 180
			if self.y != 448:
				self.y += self.speed*4
			if self.y > 448:
				self.playerimg = pygame.transform.rotate(self.playerimg, 180)
				self.y = 448


	def col(self):
		for i in allrects:
			if self.rect.colliderect(allrects.get(i)):
				pygame.draw.rect(screen,[255,0,255],[0,0,640,480])
				if not self.god:
					self.health -= 1
					self.god = True
		if self.god:
				if self.count >= 0:
					self.count -=1
				else:
					self.count = 30
					self.god = False


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

		pygame.draw.rect(screen,[255,0,255],self.rect)
		

	def random(self):
		if self.rect[0] < -40:
			self.rect[0] = 1000
			
			self.rect[1] = random.choice([0,random.randint(64,416)])
			if self.rect[1] == 0:
				self.rect[3] = random.randint(60,416)
			if self.rect[1] == 64:
				self.rect[3] = 480
