# Pygame CYOA
# Albert D, Varun G, Ivan W
# May 9, 2022
# Metadata

import pygame
from player import Player, Object
from screen import Screen
from interface import Interface
from dialogue import Dialogue

# declare global variables
global screen
global player
global objectList
global interface
global frame

pygame.init()

# extract full-screen width and height
infoObject = pygame.display.Info()

# initialize global variables
screen = Screen(pygame.image.load('Assets/final-bg-empty.png'), (5760, 3240), 0, 0, infoObject.current_w, infoObject.current_h)
player = Player(250, 250, 50, 25, 'Assets/Varun/U_moving/1.png', 10)
player.sprite = pygame.transform.scale(pygame.image.load('Assets/Varun/U_moving/1.png'), (100, 100))
objectList = []
interface = Interface('Assets/wood.jpg', [])
frame = 0