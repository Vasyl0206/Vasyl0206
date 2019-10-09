import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game")

x=225
y=225
r=50
vol=20
done = True
clock = pygame.time.Clock()



while done:
    pygame.time.delay(100)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=False
    
    x += vol
    if x>500-r-vol:
        vol = vol * (-1)
    elif x<vol+r and vol<0:
        vol = vol * (-1)
    
            
    screen.fill((0,0,0)) 
    pygame.draw.circle(screen, (255,0,0), (x,y),r)
    pygame.display.update()

    
    
    pygame.display.update()
#   clock.tick(60)

