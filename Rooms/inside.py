# Pygame CYOA
# Albert D, Varun G, Ivan W
# May 9, 2022
# Inside corridor

import pygame
import sys
sys.path.append('../AG22_4')
from player import Object, Player
from dialogue import Dialogue
pygame.init()


def penDialogue(player, objectList, screen, interface):         # Interact with pen item
    text = Dialogue('times new roman', 32, 'WHITE',
                    ['Hey, that\'s a cool pen...',
                     'Pen has been added to your inventory.'],
                    ['Varun', ''],
                    [VARUN,TRANSPARENT])
    text.play_dialogue(player, objectList, screen, interface)
    interface.items.append(penIcon)
    objectList.remove(pen)

'''Functions to enter different rooms (changes to instance variables are necessary
to specify location in new area)'''

def enterFriend(player, objectList, screen, interface):
    player.x = 700
    player.y = 900
    player.scale = 1.2
    player.direction = 'U'
    return 'friend'

def enterOutside(player, objectList, screen, interface):
    player.x = 5650
    player.y = 1270
    player.scale = 1
    player.direction = 'L'
    return 'outside'

def enterStranger(player, objectList, screen, interface):
    player.x = 1000
    player.y = 1270
    player.direction = 'L'
    player.scale = 4
    return 'stranger'

def enterReception(player, objectList, screen, interface):
    player.x = 960
    player.y = 1000
    player.direction = 'L'
    player.scale = 1.2
    return 'reception'

# Draw items (walls, doors, pen)

MUSIC = 'Assets/Celeste.mp3'
wall_1 = Object(0,0,10457,247,'Assets/transparent_image.png', None)
wall_2 = Object(0,866,10457,214, 'Assets/transparent_image.png', None)
wall_3 = Object(-50,0,50,1080,'Assets/transparent_image.png', enterOutside)

mult_factor = 4.5567 # factor for scaling
door_1 = Object(238*mult_factor,51*mult_factor-90,33*mult_factor,100, 'Assets/transparent_image.png', enterFriend)
door_2 = Object(613*mult_factor, 195*mult_factor, 33*mult_factor, 100, 'Assets/transparent_image.png', enterStranger)
door_3 = Object(990*mult_factor, 51*mult_factor-90, 33*mult_factor, 100, 'Assets/transparent_image.png', enterReception)

penIcon = pygame.transform.smoothscale(pygame.image.load('Assets/pen.png'), (500,500))
pen = Object(3000, 500, 34, 38, 'Assets/pen.png', penDialogue)
OBJECTLIST = [door_1, door_2, door_3, wall_1, wall_2, wall_3, pen]

BGSIZE = (5230, 1080)
infoObject = pygame.display.Info()

VARUN = pygame.transform.smoothscale(pygame.transform.flip(pygame.image.load('Assets/varun-agv.png'), True, False), (327.5, 595))
TRANSPARENT = pygame.image.load('Assets/transparent_image.png')
BACKGROUND = pygame.transform.scale(pygame.image.load('Assets/backgrounds/corridor-bg.png'), (10457,1080))