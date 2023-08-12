# Pygame CYOA
# Albert D, Varun G, Ivan W
# May 9, 2022
# Stranger (bathroom)

import pygame
import sys
sys.path.insert(0, './')
from player import Object, Player
from dialogue import Dialogue
import interface as mapInterface

def background(player, objectList, screen, interface):          # Turn light on
    screen.background =  pygame.transform.scale(pygame.image.load('Assets/backgrounds/bathroom.png'), BGSIZE)
    objectList.pop(2)
    objectList.append(Object(30,1500,110,110,'Assets/switch-on.png', background2))

def background2(player, objectList, screen, interface):         # Turn light off
    screen.background =  pygame.transform.scale(pygame.image.load('Assets/backgrounds/bathroom-dark.png'), BGSIZE)
    objectList.pop(2)
    objectList.append(Object(30,1500,110,110,'Assets/switch-off.png', background))

def goBack(player, objectList, screen, interface):              # Return to corridor
    player.x = 2850
    player.y = 770
    player.direction = 'U'
    player.scale = 1
    return 'inside'

def stranger_dialogue(player, objectList, screen, interface):   # Talk to the stranger
    text = Dialogue('times new roman', 32, 'WHITE', 
                    ['Thanks for turning on the light!'], 
                     ['Stranger'], 
                     [STRANGER])
    
    text.play_dialogue(player, objectList, screen, interface)
    num, choice = text.display_choices(['It wasn\'t for you!', ' No problem!'], [True, True], player, objectList, screen, interface)

    if num == 1:
        text.dialogue = [choice, 'As a token of my gratitude, here is a washcloth!', 'A washcloth has been added to your inventory.']
        text.characters = ['Varun', 'Stranger', '']
        text.sprites = [VARUN, STRANGER, TRANSPARENT]
        text.play_dialogue(player, objectList, screen, interface)
        if not (cloth_sprite in interface.items):
            interface.items.append(cloth_sprite)
    else:
        text.dialogue = [choice, 'That\'s not very nice!']
        stranger_dialogue(player, objectList, screen, interface)
    
    
MUSIC = 'Assets/Celeste.mp3'
PLAYERDIRECTION = 'U'
mult_factor = 1.2

# Background (light on/off)
BGSIZE = (2130,1770)
BACKGROUND = pygame.transform.scale(pygame.image.load('Assets/backgrounds/bathroom-dark.png'), BGSIZE)
light = Object(30,1500,110,110,'Assets/switch-off.png', background)

# Characters and sprite objects
STRANGER = pygame.transform.scale(pygame.image.load('Assets/stranger.png'), (500, 500))
VARUN = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/varun-agv.png'), True, False), (327.5, 595))
TRANSPARENT = pygame.image.load('Assets/transparent_image.png')
cloth_sprite = pygame.transform.smoothscale(pygame.image.load('Assets/washcloth.png'), (500, 500))
stranger = Object(200, 300, 400, 400, 'Assets/stranger.png', stranger_dialogue)
exit = Object(0,1700,350, 30,'Assets/transparent_image.png', goBack)
OBJECTLIST = [stranger, exit, light]