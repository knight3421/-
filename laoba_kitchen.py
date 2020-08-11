import pygame
import sys
from settings import Settings
import game_functions as gf
from laoba import Laoba
from pygame.sprite import Group
from baba import Baba
from baba import Baba
from mianbao import Mianbao
from ningmeng import Ningmeng
from fulu import Fulu
from choudoufu import Choudoufu
from game_stats import GameStats
from shou import Shou
from shou2 import Shou2
from button import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("老八厨房")
    pygame.key.set_repeat(1, 0)
    
    stats = GameStats(ai_settings)
    laoba = Laoba(screen)
    baba = Baba(ai_settings, screen)
    mianbao = Mianbao(ai_settings, screen)
    choudoufu = Choudoufu(ai_settings, screen)
    fulu = Fulu(ai_settings, screen)
    ningmeng = Ningmeng(ai_settings, screen)
    baba = Baba(ai_settings, screen)
    shou = Shou(screen,laoba,ai_settings)
    shou2 = Shou2(screen,laoba,ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    
    play_button = Button(ai_settings,screen,"Play")
    
    pygame.display.update()
    materials = Group()
    hands = Group()
    hands2 = Group()
    num_baba = []
    num_materials = []
    
    while True:
        
        gf.check_events(screen, laoba, hands, hands2, ai_settings,stats,play_button,materials,mianbao, choudoufu, fulu, ningmeng, baba,num_baba,num_materials)
        
        if stats.game_active:
            gf.update_materials(materials,laoba, ai_settings, screen,stats,shou,shou2,num_baba,num_materials,hands,hands2,sb)
            
            gf.update_hands(hands, screen,laoba, materials)
            gf.update_hands2(hands2, screen,laoba, materials)
            
        
        gf.update_screen(ai_settings, screen, laoba,mianbao, choudoufu, fulu, ningmeng, baba, hands,hands2 ,materials,stats,play_button,sb)
        
                
        
        
run_game()