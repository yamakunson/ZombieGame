import pygame,sys
from button import Button
from chess import ChessGame

pygame.init()
SCREEN=pygame.display.set_mode((1280,720))
pygame.display.set_caption("Menu")
BG=pygame.image.load("bg.png")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("PressStart2P-Regular.ttf", size)

def play():
    while True:
        ChessGame()
        pygame.display.update()

def mainMenu():
    pygame.display.set_caption("Menu")
    while True:
        SCREEN.blit(BG,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT= get_font(100).render("MAIN MENU",True,"#b68f40")
        MENU_RECT=MENU_TEXT.get_rect(center=(640,100))

        PLAY_BUTTON = Button(image=pygame.image.load("playButtonImg.png"), pos=(640, 250), text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()

        pygame.display.update()



mainMenu()