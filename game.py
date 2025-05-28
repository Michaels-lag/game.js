import pygame
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
pPos = pygame.Vector2(250, 250)

while(running):
    dt = clock.tick(120) / 1000
    
    pygame.display.flip()
    
    screen.fill("black")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.draw.rect(screen, "red", (int(pPos.x), int(pPos.y), 25, 25))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pPos.y -= 50 * dt
    if keys[pygame.K_s]:
        pPos.y += 50 * dt
    if keys[pygame.K_a]:
        pPos.x -= 50 * dt
    if keys[pygame.K_d]:
        pPos.x += 50 * dt
    
    pygame.display.update()
