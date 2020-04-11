import pygame  
import Class
import Menu
import random

pygame.init()
FPS = 45
clock = pygame.time.Clock()
toppoints = 0
playerimg = pygame.image.load("grob.png")
playerimg = pygame.transform.scale(playerimg, (32, 30))
screen = pygame.display.set_caption("-GROB-")
screen = pygame.display.set_mode([640,480])

menuglados = Menu.loadmenu("robots_ftw.ogg");

P1 = Class.Grob(64,380,5,10,"running")
T  = Class.Block(400,10,40,-400,"a001")
T1 = Class.Block(600,0,40,400,"a002")
T2  = Class.Block(800,0,40,400,"a003")
T3 = Class.Block(1000,0,40,400,"a004") 
T4  = Class.Block(1200,0,40,400,"a005")

menuglados.playsnd()
while menuglados.run:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			menuglados.run = False

	screen.fill((255,255,255))
	if menuglados.menu == 0:
		menuglados.load()
		P1.health = 5
		P1.speed = 10
		P1.state = 2
		P1.meters = 0
	elif menuglados.menu == 1:
		if P1.health <= 0:
			menuglados.menu = 0
		P1.move()
		P1.col()

		T.draw()
		T1.draw()
		T2.draw()
		T3.draw()
		T4.draw()

		T.random()
		T1.random()
		T2.random()
		T3.random()  
		T4.random() 
		pygame.draw.rect(screen,[0,0,0],[0,0,640,32])
		pygame.draw.rect(screen,[0,0,0],[0,464,640,32])

	pygame.display.update()
pygame.quit()
