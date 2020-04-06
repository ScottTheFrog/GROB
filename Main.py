import pygame  
import Class
import random
pygame.init()
run = True  
clock = pygame.time.Clock()
FPS = 45
playerimg = pygame.image.load("grob.png")
screen = pygame.display.set_caption("-GROB-")
screen = pygame.display.set_mode([640,480])


P1 = Class.Grob(64,380,1,11,"running")
T  = Class.Block(400,10,40,400,"a001")
T1 = Class.Block(600,10,40,400,"a002")
T2  = Class.Block(800,10,40,400,"a003")
T3 = Class.Block(1000,10,40,400,"a004")
T4  = Class.Block(1200,10,40,400,"a005")

	
while run:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	screen.fill((255,255,255))

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

	screen.blit(playerimg,P1.rect)

	pygame.display.update()
pygame.quit()