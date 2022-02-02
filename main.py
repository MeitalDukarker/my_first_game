import pygame

# screen size 
WINDOW_W = 900
WINDOW_H = 700
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My First Game")


# www.pngaaa.com
bk_image = pygame.image.load("background.jpg")
ship_image = pygame.image.load("ship.png")
ship_image = pygame.transform.scale(ship_image, (50, 80)) 
laser_image = pygame.image.load("laser2.png")
laser_image = pygame.transform.scale(laser_image, (10, 20)) 
clock = pygame.time.Clock()

circle_x = 10
circle_y = WINDOW_H /2
ship_x = WINDOW_W /2
ship_y = WINDOW_H - 80

circle_x_step = 10
x_step = 10
laser_list = []
play = True

EXPLOSION= "explosion.mp3"

total=0
def is_laser_hit(laser_pos):
  return abs(laser_pos[0]-circle_x) <50 and abs(laser_pos[1]-circle_y) <50
# prints all the laser on the screen
def print_lasers():
  global total
  global circle_x
  for i in range(len(laser_list)):
    laser = laser_list[i]
    screen.blit(laser_image,(laser[0],laser[1]))
    laser_list[i] = [laser[0],laser[1]-30]
    if is_laser_hit(laser):
      print("hit")
      pygame.mixer.init()
      pygame.mixer.music.load(EXPLOSION)
      pygame.mixer.Channel(2).play(pygame.mixer.Sound(EXPLOSION))
      total+=1
      circle_x = 0 

  if len(laser_list) > 0 and laser_list[0][1] < 0:
    laser_list.remove(laser_list[0])

GUN_SHOOT= "Gun shoot..mp3"
SOUND_FILE= "SONG.mp3"
pygame.mixer.init()
pygame.mixer.music.load(SOUND_FILE)
pygame.mixer.music.load(GUN_SHOOT)
pygame.mixer.Channel(0).play(pygame.mixer.Sound(SOUND_FILE))

WHITE=(255,255,255)
while play:
  screen.blit(bk_image,(0,0))
  font = pygame.font.SysFont(None, 72)
  img = font.render('Score:' +str(total),True, WHITE)
  screen.blit(img, (60, 40))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      play = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        ship_x -= x_step
      if event.key == pygame.K_RIGHT:
        ship_x += x_step
      if event.key == pygame.K_SPACE:
        laser_list.append([ship_x+21,ship_y])
        laser_list.append([ship_x+21,ship_y-20])
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(GUN_SHOOT))

        

  screen.blit(ship_image,(ship_x,ship_y))
  pygame.draw.circle(screen,(255,255,255),(circle_x , circle_y),20)
  print_lasers()

  circle_x +=circle_x_step
  if circle_x > WINDOW_W:
    circle_x_step = -10
  if circle_x <0 :
    circle_x_step = 10
  
  pygame.display.flip()


  clock.tick(50)


pygame.quit()