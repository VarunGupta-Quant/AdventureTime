# Pygame CYOA
# Albert D, Varun G, Ivan W
# May 9, 2022
# Friend (office room)

import pygame
import sys
sys.path.insert(0, './')
from player import Object, Player
from dialogue import Dialogue

def goBack(player, objectList, screen, interface):                  # Return to inside corridor
    player.x = 1160
    player.y = 275
    player.direction = 'D'
    player.scale = 1
    return 'inside'

def friend_dialogue(player, objectList, screen, interface):         # Interact with the friend
    text = Dialogue('times new roman', 32, 'WHITE', 
                    ['Oh... hi, Varun!', 
                     'I\'m really very happy to see you!',
                      'How are you doing today?'], 
                     ['Friend', 'Friend', 'Friend'], 
                     [FRIEND, FRIEND, FRIEND])
    
    text.play_dialogue(player, objectList, screen, interface)
    num, choice = text.display_choices(['Terrible. I’m feeling really worried today!', 'Good! I can’t wait for my interview!'], [True, True], player, objectList, screen, interface)

    if num == 1:    # Correct answer
        text.dialogue = [choice, 'Great! Oh, but you look a little under-dressed. Here’s my tie.', 'A tie has been added to your inventory.']
        text.characters = ['Varun', 'Friend', '']
        text.sprites = [VARUN, FRIEND, TRANSPARENT]
        text.play_dialogue(player, objectList, screen, interface)
        if not (tie_sprite in interface.items):
            interface.items.append(tie_sprite)
    else:           # Incorrect answer
        text.dialogue = [ choice, 'You won\'t do well with that attitude!']
        text.characters = ['Varun', 'Friend', '', '']
        text.sprites = [VARUN, FRIEND, TRANSPARENT, TRANSPARENT]
        text.play_dialogue(player, objectList, screen, interface)
        
PLAYERDIRECTION = 'U'
BGSIZE = (187*13.5,1080)
mult_factor = 1.2
BACKGROUND = pygame.transform.scale(pygame.image.load('Assets/backgrounds/friend-room.png'), BGSIZE)
FRIEND = pygame.transform.scale(pygame.image.load('Assets/friend.png'), (500, 500))
VARUN = pygame.transform.scale(pygame.transform.flip(pygame.image.load('Assets/varun-agv.png'), True, False), (327.5, 595))
TRANSPARENT = pygame.image.load('Assets/transparent_image.png')
MUSIC = 'Assets/Celeste.mp3'
friend = Object(1900, 300, 150, 150, 'Assets/friend.png', friend_dialogue)
exit = Object(625,920,200,30,'Assets/transparent_image.png', goBack)
tie_sprite = pygame.transform.smoothscale(pygame.image.load('Assets/tie.png'), (500, 500))

# Walls to constrain player movement
wall_1 = Object(0,215,10457,0,'Assets/transparent_image.png', None)
wall_2 = Object(0,600,600,0, 'Assets/transparent_image.png', None)
wall_3 = Object(600,600,0,340,'Assets/transparent_image.png', None)
wall_4 = Object(850,600,0,340, 'Assets/transparent_image.png', None)
wall_5 = Object(850,600,10457,0, 'Assets/transparent_image.png', None)
wall_6 = Object(2470,0,0,600, 'Assets/transparent_image.png', None)
wall_7 = Object(300,330,0,155,'Assets/transparent_image.png', None)
wall_8 = Object(1150,330,0,270, 'Assets/transparent_image.png', None)
wall_9 = Object(300,330,850,0,'Assets/transparent_image.png', None)
wall_10 = Object(300,485,850,0, 'Assets/transparent_image.png', None)
OBJECTLIST = [friend, wall_1, wall_2, wall_3, wall_4, wall_5, wall_6, wall_7, wall_8, wall_9, wall_10, exit]
