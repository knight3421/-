import pygame
from pygame.sprite import Sprite

class Shou(Sprite):
    def __init__(self,screen,laoba,ai_settings):
        super().__init__()
        
        self.screen = screen
        self.image = pygame.image.load('images/youshou.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = laoba.rect.left
        self.rect.top = laoba.rect.bottom
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.shou_speed_factor
        
    def update(self,laoba):
        
        
        self.y += self.speed_factor
        self.rect.y = self.y
        
        self.rect.move(laoba.rect.x,self.y)
        
        
    def use_youshou(self,laoba):
        
        self.screen.blit(self.image, self.rect)
     