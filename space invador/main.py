import pygame
import sys
import random

pygame.init()
pygame.mixer.init()
# alll game varibles 

run = True
SCREEN_HEIGHT , SCREEN_WIDTH = 600,800
FPS = 60
icon_img =pygame.image.load("Assets/images/ufo.png")
bg_img = pygame.image.load("Assets/images/background.png")
ship_img = pygame.image.load("Assets/images/player.png")
inv_img = pygame.image.load("Assets/images/enemy.png")
bullet_img = pygame.image.load("Assets/images/bullet.png")
shipx = 400
shipy = 550
enemy_lis = []
bullet_lis = []
invx , invy = 0,0
enemy_speed = 4
max_bullet = 5
score = 0 
text_font = pygame.font.SysFont("Arial", 50)
game_font = pygame.font.SysFont("Arial", 100)
pygame.mixer.music.load("Assets/music/background.wav")
pygame.mixer.music.play(loops=1000)
bullet_music = pygame.mixer.Sound("Assets/music/laser.wav")
explosion_music = pygame.mixer.Sound("Assets/music/explosion.wav")
# basic screen setup 


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Space Invadors")
pygame.display.set_icon(icon_img)
clock = pygame.time.Clock()

# spaceship part 

def spaceship(x,y):
  ship_rect = ship_img.get_rect(center =(shipx,shipy))
  screen.blit(ship_img,ship_rect)

# enemy part 

for i in range(0, 10):
  
  invx , invy = random.randint(30,770),random.randint(30,450)
  enemy_rect = ship_img.get_rect(center =(invx,invy))
  enemy_lis.append(enemy_rect)
def enemy():
   for i in enemy_lis:
    screen.blit(inv_img,i)

def enemy_motion():
   global enemy_speed
   for enemy in enemy_lis:
      enemy.x-=enemy_speed
      if enemy.x <-60 :
         enemy.x = 800
         enemy.y +=30
   
# bullet part 

def bullet():
  if len(bullet_lis) <max_bullet :
   bullet_rect= bullet_img.get_rect(center = (shipx,shipy))
   bullet_lis.append(bullet_rect)
   bullet_music.play()
  
def bullet_motion():
    for bullet in bullet_lis :
       bullet.y-=10
       if bullet.y < 0 :
          bullet_lis.remove(bullet)
       screen.blit(bullet_img,bullet)

# game over part 

def game_over():
     global enemy_speed , max_bullet
     game_over = game_font.render("Game Over", True,(255,255,255))
     screen.blit(game_over,(200,200))
     enemy_speed = 0
     max_bullet = 0


# collision part 

def collision():
   global score
   for enemy in enemy_lis:
      if enemy.y >= SCREEN_HEIGHT-150 : 
            game_over()
   for bullet in bullet_lis:
      for enemy in enemy_lis:
         if pygame.Rect.colliderect(bullet,enemy):
            explosion_music.play()
            if bullet in bullet_lis:
             bullet_lis.remove(bullet)  
            enemy_lis.remove(enemy)  
            score+=1
            invx , invy = random.randint(30,770),random.randint(30,450)
            enemy_rect = ship_img.get_rect(center =(invx,invy))
            enemy_lis.append(enemy_rect)
             
# score part 

def display_score():
    score_text = text_font.render(str(score), True, (255, 255, 255))
    screen.blit(score_text, (700,0))
    


# main part 

def main():
 global shipx,shipy , bulx , buly
 while run :
  screen.blit(bg_img,(0,0))
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    if event.type == pygame.KEYDOWN:
     if event.key == pygame.K_SPACE:
        bullet()
  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT] and shipx>30:
        shipx -= 5
  if keys[pygame.K_RIGHT]and shipx<770:
        shipx += 5
  

  spaceship(shipx,shipy)
  enemy()
  enemy_motion()
  bullet_motion()
  collision()
  display_score()
  pygame.display.update()
  clock.tick(FPS)
if __name__ =="__main__":
    main()