import pygame
from pygame.sprite import Sprite
from laoba import Laoba
from shou import Shou
from shou2 import Shou2
from time import sleep

class Baba(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        self.image = pygame.image.load('images/baba.bmp')
        
        
        
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.y = float(self.rect.y)
        
      
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def update(self,screen,ai_settings,laoba,stats,shou,shou2,num_baba,num_materials,hands,hands2):
        shou = Shou(screen,laoba,ai_settings)
        shou2 = Shou2(screen,laoba,ai_settings)
        self.y += self.ai_settings.baba_speed_factor
        self.rect.y = self.y
         
        if pygame.sprite.collide_rect(self,laoba)==1:
            loser = pygame.image.load('images/loser.png')
            screen.blit(loser,(0,0))
            pygame.display.flip()
            
            pygame.mixer.pre_init()
            pygame.mixer.init()
            pygame.mixer.stop()
            b = pygame.mixer.Sound('music/吃粑粑.wav')
            b.play()
            sleep(12.0)
           
            stats.game_active = False
            pygame.mouse.set_visible(True)
        
        if pygame.sprite.spritecollide(self,hands,False):
            num_baba.append('baba')
            pygame.mixer.pre_init()
            pygame.mixer.init()
            b = pygame.mixer.Sound('music/粑粑.wav')
            b.play()
        if pygame.sprite.spritecollide(self,hands2,False):
            num_baba.append('baba')
            pygame.mixer.pre_init()
            pygame.mixer.init()
            b = pygame.mixer.Sound('music/粑粑.wav')
            b.play()