import sys
import pygame
from shou import Shou
from shou2 import Shou2
from baba import Baba
from mianbao import Mianbao
from ningmeng import Ningmeng
from fulu import Fulu
from choudoufu import Choudoufu
from laoba import Laoba
from time import sleep
from game_stats import GameStats

import random
def check_events(screen, laoba, hands, hands2, ai_settings,stats,play_button,materials,mianbao, choudoufu, fulu, ningmeng, baba,num_baba,num_materials):
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:#监控键盘事件
           
            if event.key ==pygame.K_d and laoba.rect.right < laoba.screen_rect.right:
                
                laoba.rect.centerx+=1
            if event.key ==pygame.K_a and laoba.rect.left >0:
                
                laoba.rect.centerx-=1
        
            if event.key ==pygame.K_w and laoba.rect.top > laoba.screen_rect.top:
                
                laoba.rect.bottom-=1
            if event.key ==pygame.K_s and laoba.rect.bottom < laoba.screen_rect.bottom:
                
                laoba.rect.bottom+=1
            if event.key ==pygame.K_ESCAPE:
                pygame.quit()
        
        elif event.type ==pygame.MOUSEBUTTONDOWN:#监控鼠标事件
            
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x,mouse_y) and not stats.game_active:
                
                pygame.mouse.set_visible(False)
                
                del num_baba[:]
                del num_materials[:]
                stats.score = 0
                stats.game_active = True
                
                pygame.mixer.pre_init()
                pygame.mixer.init()
                x = pygame.mixer.Sound('music/BGM.wav')
                pygame.mixer.stop()
                b = pygame.mixer.Sound('music/intro.wav')
                b.play(-1,0,0)
                
                
                hands.empty()
                hands2.empty()
                materials.empty()
                create_fleet(mianbao, choudoufu, fulu, ningmeng, baba, ai_settings, screen, materials)
                laoba.center_laoba()
            
            
            if event.button == 1:
                laoba_youshou(screen, laoba, hands,hands2, ai_settings)
                pygame.mixer.pre_init()
        
                pygame.mixer.init()
        
                x = pygame.mixer.Sound('music/奥里给.wav')
                x.set_volume(0.5)
                x.play()
            if event.button == 3:
                laoba_zuoshou(screen, laoba,hands, hands2, ai_settings)
                pygame.mixer.pre_init()
        
                pygame.mixer.init()
        
                x = pygame.mixer.Sound('music/造它就完了.wav')
                x.set_volume(0.5)
                x.play()
def laoba_youshou(screen, laoba, hands,hands2, ai_settings):
    if len(hands)+len(hands2) < ai_settings.hands_allowed:
        new_shou = Shou(screen,laoba,ai_settings)
        hands.add(new_shou)
        
def laoba_zuoshou(screen, laoba,hands, hands2, ai_settings):
    if len(hands2)+len(hands) < ai_settings.hands_allowed:
        new_shou = Shou2(screen,laoba,ai_settings)
        hands2.add(new_shou)
        hands.empty()
def update_hands(hands, screen,laoba, materials):
    hands.update(laoba)
    for shou in hands.copy():
        if shou.rect.top >= laoba.screen_rect.bottom:
            hands.remove(shou)
         
    
    collisions = pygame.sprite.groupcollide(hands,materials,True,True)
    
def update_hands2(hands2, screen,laoba, materials):
    hands2.update(laoba)
    for shou2 in hands2.copy():
        if shou2.rect.bottom <= laoba.screen_rect.top:
            hands2.remove(shou2)    
    collisions = pygame.sprite.groupcollide(hands2,materials,True,True)
    
def update_materials(materials,laoba, ai_settings, screen,stats,shou,shou2,num_baba,num_materials,hands,hands2,sb):
    materials.update(screen,ai_settings,laoba,stats,shou,shou2,num_baba,num_materials,hands,hands2)
    for material in materials.sprites():
        if material.rect.top >= laoba.screen_rect.bottom:
            materials.remove(material)
            
    collide_list = pygame.sprite.spritecollide(laoba,materials,True)
    
    if stats.game_active:
        
        stats.score = len(num_materials)-len(num_baba)
    elif not stats.game_active:
        stats.score = 0
    sb.prep_score() 
    check_high_score(stats,sb)    
    
        

    
def update_screen(ai_settings, screen, laoba,mianbao, choudoufu, fulu, ningmeng, baba, hands, hands2,materials,stats,play_button,sb):
    
        
    screen.fill(ai_settings.bg_color)
    many_materials(mianbao, choudoufu, fulu, ningmeng, baba, ai_settings, screen, materials)    
    for shou in hands.sprites():
        shou.use_youshou(laoba)
    for shou2 in hands2.sprites():
        shou2.use_zuoshou(laoba) 
    
   
    materials.draw(screen)
    
    laoba.blitme()
    sb.show_score()
    if not stats.game_active:
        pygame.mixer.pre_init()
        
        pygame.mixer.init()
        
        
        
        x = pygame.mixer.Sound('music/BGM.wav')
        x.set_volume(0.2)
        x.play(-1,0,0)
        b = pygame.mixer.Sound('music/嘿嘿，来了啊.wav')
        b.play()
        
        
        
        bg_pic = pygame.image.load('images/bg_pic.png')
        screen.blit(bg_pic,(0,0))
        play_button.draw_button()
    pygame.display.flip()
def creat_baba(ai_settings, screen,baba, materials):
    baba = Baba(ai_settings,screen)
    baba_w = baba.rect.width
    baba.x = baba_w + 2*baba_w*i

    

    
    
        
def create_fleet(mianbao, choudoufu, fulu, ningmeng, baba, ai_settings, screen, materials):
     #加载参数
    m_width = 20
    
    
    
    for i in range(9):
        laoba = Laoba(screen)
        baba = Baba(ai_settings, screen)
        mianbao = Mianbao(ai_settings, screen)
        choudoufu = Choudoufu(ai_settings, screen)
        fulu = Fulu(ai_settings, screen)
        ningmeng = Ningmeng(ai_settings, screen)
        m = random.randint(1,5)
        if m == 1:
            
            mianbao.rect.x = 2 * m_width * i
            materials.add(mianbao)
        if m == 2:
            
            choudoufu.rect.x = 2 * m_width * i
            materials.add(choudoufu)
        elif m == 3:
            
            fulu.rect.x = 2 * m_width * i
            materials.add(fulu)
        elif m == 4:
            
            ningmeng.rect.x = 2 * m_width * i
            materials.add(ningmeng)
        elif m == 5:
            
            baba.rect.x = 2 * m_width * i
            materials.add(baba)
            
def many_materials(mianbao, choudoufu, fulu, ningmeng, baba, ai_settings, screen, materials):
    if len(materials) == 0:
        create_fleet(mianbao, choudoufu, fulu, ningmeng, baba, ai_settings, screen, materials)#生成一行材料
        
def check_high_score(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

