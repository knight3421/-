import pygame
from pygame.sprite import Sprite
from laoba import Laoba
from shou import Shou
from shou2 import Shou2

class Mianbao(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load('images/mianbao.bmp')
        
        self.rect = self.image.get_rect()
        
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.y = float(self.rect.y)
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def update(self,screen,ai_settings,laoba,stats,shou,shou2,num_baba,num_materials,hands,hands2):
        shou = Shou(screen,laoba,ai_settings)
        shou2 = Shou2(screen,laoba,ai_settings)
        self.y += self.ai_settings.mianbao_speed_factor 
        self.rect.y = self.y
        if pygame.sprite.spritecollide(self,hands,False):
            num_materials.append('mianbao')
            pygame.mixer.pre_init()
            pygame.mixer.init()
            b = pygame.mixer.Sound('music/汉堡.wav')
            b.play()
        if pygame.sprite.spritecollide(self,hands2,False):
            num_materials.append('mianbao')
            pygame.mixer.pre_init()
            pygame.mixer.init()
            b = pygame.mixer.Sound('music/汉堡.wav')
            b.play()