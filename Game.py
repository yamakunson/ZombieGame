import sys
import pygame
import random
import zombie
# Initialize Pygame

def ZombieGame():

    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    #pygame.mouse.set_cursor(pygame.cursors.broken_x)
    font = pygame.font.Font('freesansbold.ttf', 32)
 
    # Define colors
    lynx_1 = pygame.transform.scale(pygame.image.load("Spite\Lynx\Lynx_1.png"), (80, 80))
    lynx_2 = pygame.transform.scale(pygame.image.load("Spite\Lynx\Lynx_2.png"), (80, 80))
    lynx_3 = pygame.transform.scale(pygame.image.load("Spite\Lynx\Lynx_3.png"), (80, 80))
    bat = pygame.transform.scale(pygame.image.load("Spite\\bat.png"), (80, 80))
    kurukuru = pygame.mixer.Sound("Kurukuru.mp3")
    kururing = pygame.mixer.Sound("Kururing.mp3")
    #pygame.mouse.set_visible(False)
    WHITE = (255, 255, 255)
    BLACK = (102, 255, 255)
    RED = (255,0,0)
    # Set the dimensions of the chessboard
    WIDTH, HEIGHT = 800, 600
    SIZE = WIDTH // 10

    # Create the game window
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)
    pygame.display.set_caption("Zombie Game")
    #screen.fill(BLACK)
    circle_list = [(WIDTH//4,3*HEIGHT//10),(2*WIDTH//4,3*HEIGHT//10),(3*WIDTH//4,3*HEIGHT//10),(3.5*WIDTH//10,7*HEIGHT//10),(6.5*WIDTH//10,7*HEIGHT//10)]
    zom_list = [None,None,None,None,None]
    point = [0,0]
    text = font.render("Hit" + str(point[0]), True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.center = (WIDTH//4-15,HEIGHT//16)
    text2 = font.render("Miss " + str(point[1]), True, (255, 0, 0))
    text2Rect = text2.get_rect()
    text2Rect.center = (WIDTH//4,HEIGHT//8)
    def draw_board():
        screen.fill(BLACK)
        for circle in circle_list:
            pygame.draw.circle(screen,WHITE,circle,HEIGHT//10,0)
        for zom in zom_list:
            if zom != None:
                screen.blit(zom.Image, pygame.Rect(circle_list[zom.num_pos][0]-SIZE/2,circle_list[zom.num_pos][1]-SIZE/2,SIZE,SIZE))
        text = font.render("Hit: " + str(point[0]) , True, (255, 0, 0))
        text2 = font.render("Miss: " + str(point[1]), True, (255, 0, 0))
        screen.blit(text, textRect)
        screen.blit(text2, text2Rect)
        
    # Game loop
    def zom_generator():
        n = 0
        list = []
        for zom in zom_list:
            if zom == None:
                list.append(n)
            n = n + 1
        if list != [] and len(list)>0:
            num = random.choice(list)       
            zom_list[num] = zombie.zombie(num)
    def checkin_circle(center):
        n = 0
        for pos in circle_list:
            if (pos[0]-center[0])**2 + (pos[1]-center[1])**2 < SIZE **2 and zom_list[n] != None and zom_list[n].status == 1:
                return n
            n = n + 1
        return -1
    def playsound():
        sound_list =[kurukuru,kururing]
        song = random.choice(sound_list) 
        pygame.mixer.Sound.play(song)
        #pygame.mixer.music.stop()
    def update():
        for zom in zom_list:
            if zom != None:
                if zom.status == 0 or zom.status == 2 :
                    zom.timeout -= 1
                else: zom.timeexist -= 1
                if zom.timeexist == 0 and zom.status == 1:
                    zom.Image = lynx_1
                    zom.status = 2
                    zom.timeout = 60
                if zom.timeout == 0:
                    if zom.status == 2:
                        point[1] += 1
                    zom_list[zom.num_pos] = None
    clock = pygame.time.Clock()
    zom_timer = 30
    running = True
    draw_board()
    while running:
        mouse = pygame.mouse.get_pos()
        if zom_timer <= 0:
            zom_generator()
            zom_timer = random.randint(30,60)
        zom_timer -= point[0]/30 + 1
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                running = False 
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_q: 
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                check = checkin_circle(mouse)
                if check != -1:
                    point[0] += 1       
                    zom_list[check].Image = lynx_2
                    zom_list[check].status = 0
                    playsound()
        update()
        draw_board()
        pygame.display.update()
        clock.tick(60)

    # Quit Pygame
    pygame.quit()
ZombieGame()
