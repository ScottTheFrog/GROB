import pygame
screen = pygame.display.set_mode([640,480])
menuimg= pygame.image.load("menu.png")
menuimg = pygame.transform.scale(menuimg, (640, 480))
class loadmenu():
	def __init__(self,song):
		self.run = True
		self.menu = True
		self.color = pygame.Color(255,0,255,25)
		self.song = song
		self.pressed = 0
		self.exit = False
		self.play = pygame.Rect(292,290,348,20)
		self.options = pygame.Rect(292,324,348,20)
		self.exit = pygame.Rect(600,400,30,30)

		sound = pygame.mixer.Sound(self.song)
		sound.play()
		sound.set_volume(0.1)
	def load(self):
		print(self.pressed)
		screen.blit(menuimg,[0,0])
		m = pygame.mouse.get_pos()
		mp = pygame.mouse.get_pressed()[0]
		mh = [2,2]
		mouse = pygame.Rect(m,mh)
		if mouse.colliderect(self.play):
			pygame.draw.rect(screen,self.color,self.play)
			self.pressed = 1
		elif mouse.colliderect(self.options):
			pygame.draw.rect(screen,self.color,self.options)
			self.pressed = 2
		elif mouse.colliderect(self.exit):
			pygame.draw.rect(screen,self.color,self.exit)
			self.pressed = 3
		else:
			self.pressed = 0

		if mp:
			if self.pressed == 1:
				self.menu = False
			if self.pressed == 3:
				self.run = False
