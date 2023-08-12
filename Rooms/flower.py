# Pygame CYOA
# Albert D, Varun G, Ivan W
# May 9, 2022
# Tutorial for game

import pygame
import sys

sys.path.insert(0, './')
from player import Object, Player
from dialogue import Dialogue
import interface as mapInterface

rose_sprite = pygame.transform.smoothscale(pygame.image.load('Assets/flower-icon.png'), (500, 500))

def flower_dialogue(player, objectList, screen, interface, bool = False):
    text = Dialogue('times new roman', 32, 'WHITE', 
                    ['Oh... how I long to be picked up...', 
                     '...', 
                     'Oh, hi! Didn\'t see you there. My name is Rose, and I have a request for you, if it\'s not too much trouble...', 
                     'Would you pluck me out of the dirt and take me with you? I\'d like to go on an adventure!'], 
                     ['Flower', 'Flower', 'Flower', 'Flower'], 
                     [FLOWER, FLOWER, FLOWER, FLOWER])
    
    text.play_dialogue(player, objectList, screen, interface)
    if bool:
        num, choice = text.display_choices(['Sure!', 'No thanks.'], [True, True], player, objectList, screen, interface)
    else:
        num, choice = text.display_choices(['Sure!', 'No thanks.'], [False, True], player, objectList, screen, interface) #Option 1 will not be available

    if num == 0:
        text.dialogue = [choice, 'Thank you so much! I will be in your care, then.  (✿◠‿◠)']
        text.characters = ['Varun', 'Flower']
        text.sprites = [VARUN, FLOWER]
        text.play_dialogue(player, objectList, screen, interface)
    else:
        text.dialogue = [ choice, 
                         'How dare you! I\'m sad now...', 
                         'Oh no! This is what happens when you choose the incorrect response. In this game, choosing the incorrect answer will force you to restart.', 
                         'Let\'s try that again, selecting the correct answer this time!']
        
        
        text.characters = ['Varun', 'Flower', '', '']
        text.sprites = [VARUN, FLOWER, TRANSPARENT, TRANSPARENT]
        text.play_dialogue(player, objectList, screen, interface)
        flower_dialogue(player, objectList, screen, interface, True) #Run again with both options available
        
        text.characters = ['', '', '']
        text.sprites = [TRANSPARENT, TRANSPARENT, TRANSPARENT]
        
        text.dialogue = ['Great job! Now, if you press "I" on your keyboard, you\'ll find your inventory. The flower is currently stored in the first slot.', 
                              'After interacting with characters, you\'ll be able to receive special items that can be stored here.',
                              'Try it out yourself! Press "I" again to close out of the inventory.']
        
        text.play_dialogue(player, objectList, screen, interface)
        
        interfaceClose = False
        pygame.event.clear
        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                # draw inventory image
                screen.screen.blit(pygame.transform.smoothscale(interface.inventory, (screen.width, screen.height)), (0, 0))
                # draw inventory grid
                interface.draw_grid(screen)
                pygame.display.update()
                break
            
        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                pygame.display.update()
                break  
            
        text.dialogue = ['Great! Now, we will show you how to view the map.', 
                              'The map will show you an outline of room locations inside the office. Refer back to the map if you get lost.',
                              'Try it out yourself! Press "M" again to close out of the inventory.']
        
        text.play_dialogue(player, objectList, screen, interface)
        
        pygame.event.clear
        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                screen.screen.blit(pygame.transform.smoothscale(mapInterface.MAP, (screen.width, screen.height)), (0, 0))
                # draw objects and player location on map
                pygame.display.update()
                break
        
        while True:
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                pygame.display.update()
                break  
            
        
        text.dialogue = ['You can also find items in the surrounding environment. These items may be key to solving a level, so keep an eye out for them!', 
                            'That\'s the end of the tutorial! Now, keep moving forward along this path...']
        
        text.play_dialogue(player, objectList, screen, interface)
        interface.items.append(rose_sprite)
        objectList.pop(0)
        """
        
        
        interfaceClose = False
        while True:
            if interface.invStatus:
                print('hey')
                interfaceClose = True
            if interfaceClose:
                if not interface.invStatus:
                    break
        
        finishText2 = Dialogue('times new roman', 32, 'WHITE', 
                              'This is your inventory. After interacting with characters, you\'ll be able to receive special items that can be stored here.')
"""
BACKGROUND = pygame.transform.scale(pygame.image.load('Assets/background_v1.png'), (5760, 3240))
FLOWER = pygame.transform.smoothscale(pygame.image.load('Assets/flower-icon.png'), (500, 500))
VARUN = pygame.transform.smoothscale(pygame.transform.flip(pygame.image.load('Assets/varun-agv.png'), True, False), (327.5, 595))
TRANSPARENT = pygame.image.load('Assets/transparent_image.png')
MUSIC = 'Assets/Celeste.mp3'
object = Object(0, 0, 100, 100, 'Assets/snorlax_sprite.webp', 'outside')
flower = Object(500, 500, 100, 100, 'Assets/flower.png', flower_dialogue)
OBJECTLIST = [object, flower]