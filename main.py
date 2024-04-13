import random
import pygame.display
from Textbutton import TButton

state = 0
times = 0
def callback():
    global state,times
    times = times + 1
    a = random.randint(0, 1)
    b = random.randint(0, 1)
    if a == 0 and b == 0:
        state = 1
    elif a == 1 and b == 1:
        state = 2
    elif a == 0 and b == 1 or a == 1 and b == 0:
        state = 3
    return state

pygame.init()
screen = pygame.display.set_mode((400, 700))
pygame.display.set_caption("圣杯模拟器")
font = pygame.font.SysFont("Times New Roman", 50)
tfont = pygame.font.SysFont("Times New Roma",30)
# import image
boundw = pygame.transform.scale(pygame.image.load("./resource/栅栏横.png").convert_alpha(), (450, 10))
boundh = pygame.transform.scale(pygame.image.load("./resource/栅栏竖.png").convert_alpha(), (10, 750))
SN = pygame.transform.scale(pygame.image.load("./resource/bExitN.png").convert_alpha(), (200, 75))
SD = pygame.transform.scale(pygame.image.load("./resource/bExitD.png").convert_alpha(), (200, 75))
SM = pygame.transform.scale(pygame.image.load("./resource/bExitM.png").convert_alpha(), (200, 75))
background = pygame.transform.scale(pygame.image.load("./resource/tb.png").convert_alpha(), (300, 400))
shengbeiZ = pygame.transform.scale(pygame.image.load("./resource/ShengBei/1.png").convert_alpha(),(100,200))
shengbeiF = pygame.transform.scale(pygame.image.load("./resource/ShengBei/2.png").convert_alpha(),(100,200))

# button
Sbutton = TButton(100, 550, "Start", SN, SM, SD, callback, font, (0, 0, 0))
running = True
while running:
    # sound
    x=random.randint(1,2)
    clicksound=pygame.mixer.Sound(f"./resource/sound/{x}.mp3")
    clicksound.set_volume(0.2)
    for event in pygame.event.get():
        mx, my = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEMOTION:
            Sbutton.getFocus(mx, my)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Sbutton.mouseDown(mx, my)
        elif event.type == pygame.MOUSEBUTTONUP:
            Sbutton.mouseUp(mx, my)
            clicksound.play()
            pygame.time.wait(10)
        pygame.display.update()
        screen.fill((255, 255, 255))
        Sbutton.draw(screen)
        screen.blit(boundw, (-25, 0))
        screen.blit(boundw, (-25, 690))
        screen.blit(boundh, (0, -25))
        screen.blit(boundh, (390, -25))
        screen.blit(background, (50, 100))
        if state == 1:
            screen.blit(shengbeiF, (100,175))
            screen.blit(shengbeiF,(210,175))
        elif state == 2:
            screen.blit(shengbeiZ, (100, 175))
            screen.blit(shengbeiZ, (210, 175))
        elif state == 3:
            screen.blit(shengbeiZ, (100, 175))
            screen.blit(shengbeiF, (210, 175))
        #text
        text = tfont.render(f"The times you clicks:{times}",True,(0,0,0))
        screen.blit(text,(95,50))
    pygame.display.flip()
