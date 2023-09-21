import pygame
lynx_1 = pygame.transform.scale(pygame.image.load("Spite\Lynx\Lynx_1.png"), (80, 80))
lynx_2 = pygame.transform.scale(pygame.image.load("Spite\Lynx\Lynx_2.png"), (80, 80))
lynx_3 = pygame.transform.scale(pygame.image.load("Spite\Lynx\Lynx_3.png"), (80, 80))
lynx_3 = pygame.transform.flip(lynx_3, True, False)
class zombie:
    def __init__(self,num_pos):
        self.Image = lynx_3
        self.status = 1
        self.HP = 1
        self.num_pos = num_pos
        self.timeout = 30
        self.timeexist = 60