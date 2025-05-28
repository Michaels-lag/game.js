import pygame
import random
#from PTL import image
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
pPos = pygame.Vector2(200, 400)
ePos = pygame.Vector2(600, 400)
eLives = 1
pLives = 1

while(running):
    dt = clock.tick(120) / 1000
    
    pygame.display.flip()
    
    screen.fill("black")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
    if pLives == 1:
        pygame.draw.rect(screen, "green", (int(pPos.x), int(pPos.y), 25, 25))
    else:
        print("You lose.")
    
    if eLives == 1:
        pygame.draw.rect(screen, "red", (int(ePos.x), int(ePos.y), 25, 25))
    else:
        print("You win!")
        running = False
        #img = Image.open("path/to/your/image.jpg")
        #img.show()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pPos.y -= 50 * dt
    if keys[pygame.K_s]:
        pPos.y += 50 * dt
    if keys[pygame.K_a]:
        pPos.x -= 50 * dt
    if keys[pygame.K_d]:
        pPos.x += 50 * dt
    if keys[pygame.K_f]:
        fP1 = random.randint(0, 800)
        fP2 = random.randint(0, 800)
        pygame.draw.rect(screen, "orange", (fP1, fP2, 25, 25))
        if (fP1 - 25 <= ePos.x <= fP1 + 25) and (fP2 - 25 <= ePos.y <= fP2 + 25):
            print("Hit, Enemy down, Good job")
            eLives = eLives - 1
            
    pygame.draw.rect(screen, "red", (int(ePos.x), int(ePos.y), 25, 25))
    
    pygame.display.update()
