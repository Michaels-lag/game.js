import pygame
import random
import os
from PIL import Image
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
run = 1
pPos = pygame.Vector2(200, 400)
ePos = pygame.Vector2(600, 400)
eLives = 1
pLives = 1
run2 = 1
attack_timer = pygame.time.get_ticks()

pygame.time.delay(1500)

while(run == 1):
    run2 = 1
    file_path = "assets/sacred_potatos.webp"
    if os.path.exists("assets/sacred_potatos.webp"):
        print("You may continue")
    else:
        print("Proceeding to crash, the sacred potatos are missing they must be found")
        break
    
    dt = clock.tick(120) / 1000
    
    pygame.display.flip()
    
    screen.fill("black")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: ##also won't work if this isn't here
            choice.lower("Would you like to quit? (y/n: )")
            
    if pLives == 1:
        pygame.draw.rect(screen, "green", (int(pPos.x), int(pPos.y), 25, 25))
    else:
        print("You lose.")
    
    if eLives == 1:
        pygame.draw.rect(screen, "red", (int(ePos.x), int(ePos.y), 25, 25))
    else:
        pygame.draw.rect(screen, "black", (int(ePos.x), int(ePos.y), 25, 25))
        print("You win!")
        pygame.time.delay(2000)
        run = 0
    
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
        fP1 = random.randint(0, 801)
        fP2 = random.randint(0, 801)
        pygame.draw.rect(screen, "orange", (fP1, fP2, 25, 25))
        if (fP1 - 25 <= ePos.x <= fP1 + 25) and (fP2 - 25 <= ePos.y <= fP2 + 25):
            print("Hit, Enemy down, Good job")
            eLives = eLives - 1
            pygame.time.delay(1500)
            
    pygame.draw.rect(screen, "red", (int(ePos.x), int(ePos.y), 25, 25))
    
    while run2 == 1:
        if pygame.time.get_ticks() - attack_timer >= 2500:
            (eAposx) = random.randint(0,801)
            (eAposy) = random.randint(0,801)
            pygame.draw.rect(screen, "orange", (int(eAposx), int(eAposy), 25, 25))
            if (eAposx - 25 <= pPos.x <= eAposx + 25) and (eAposy - 25 <= pPos.y <= eAposy + 25):
                print("You lose")
                pLives = pLives - 1
                run = 0
        run2 = 0
    
    pygame.display.update()
    
for event in pygame.event.get(): ##if this isn't here it wont work idk why
        if event.type == pygame.QUIT:
            choice.lower("Would you like to quit? (y/n: )")
            if choice.lower == "y":
                running = False
                pygame.quit()
                
pygame.draw.rect(screen, "black", (int(ePos.x),int(ePos.y), 25, 25))
pygame.time.delay(2000)  # Let user see the message
pygame.quit()
if os.path.exists("assets/sacred_potatos.webp") and pLives == 1:
    img = Image.open("assets/hit.png")
    img.show()
    pygame.time.delay(5000)
    img = Image.open("assets/you win.png")
    img.show()
else:
    pygame.time.delay(2000)
    img = Image.open("assets/lose.png")
    img.show()
