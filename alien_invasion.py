import sys
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from scoreboard import Scoreboard
import game_functions as gf
from pygame.sprite import Group

def run_game():
    #初始化游戏并创建一个游戏对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建play按钮
    play_button = Button(ai_setting,screen,"New Game")

    #创建实例
    ship = Ship(ai_setting,screen)
    aliens = Group()
    bullets = Group()
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting,screen,stats)
    gf.create_fleet(ai_setting,screen,ship,aliens)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_setting,screen,stats,sb,play_button,ship,aliens,bullets)
        
        if stats.game_active:
                ship.update()
                gf.update_aliens(ai_setting,screen,stats,sb,ship,aliens,bullets)
                gf.update_bullets(ai_setting,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_setting,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()