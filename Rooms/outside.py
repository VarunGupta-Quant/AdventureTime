# Pygame CYOA
# Albert D, Varun G, Ivan W
# May 9, 2022
# Outside area

import pygame
import sys
sys.path.append('../AG22_4')
from dialogue import Dialogue
from interface import Interface
from player import Object, Player
from flower import flower_dialogue

pygame.init()


snorlax_dialogue = Dialogue('times new roman', 
                            32, 
                            'WHITE', 
                            ['why hello there sir!', 
                            'why, thank you for saying that!', 
                            'nice weather we\'re having today', 
                            'yeah, i think so too'], 
                            ['joker', 'ryuji', 'joker', 'ryuji'], 
                            [CHAR_SPRITE1, CHAR_SPRITE2, CHAR_SPRITE1, CHAR_SPRITE2])

def key_dialogue(player, objectList, screen, interface):
    text = Dialogue('times new roman', 32, 'WHITE', 
                        ['Oh neato, a key! I wonder what it could be used for...',
                         '...',
                         'Pick me up...',
                         'I wish to return to my master...',
                         'Key has been added to your inventory.'], 
                        ['Varun', 'Key', 'Key', 'Key',''], [VARUN, key_sprite, key_sprite, key_sprite, TRANSPARENT])
    
    text.play_dialogue(player, objectList, screen, interface)
    interface.items.append(key_sprite)
    objectList.pop(objectList.index(key))

def enterRoom(player, objectList, screen, interface):
    if key_sprite in interface.items:   # Check if player has at least two items in inventory
        player.x = 10
        player.y = 540
        player.direction = 'R'
        return "inside"
    else:                               # Alert player that the building cannot be entered yet
        text = Dialogue('times new roman', 32, 'WHITE', 
                        ['It looks like you don\'t have the KEY to enter...',
                         'Look along the path for another item.'], 
                        ['',''], [TRANSPARENT, TRANSPARENT])
    
        text.play_dialogue(player, objectList, screen, interface)
           

# Objects for outside area

rose_flower = Object(560*3,414*3,9*3,15*3,'Assets/interactables/flower.png', flower_dialogue)
key = Object(1121*3, 420*3, 8*3, 4*3, 'Assets/interactables/key.png', key_dialogue)
doorEntrance = Object(1911*3, 392*3, 9*3, 62*3, 'Assets/transparent_image.png', enterRoom)
ROOMCHANGE = [1911*3, 392*3, 9*3, 62*3]
OBJECTLIST = [rose_flower, key, doorEntrance]
PLAYERDIRECTION = 'R'
BGSIZE = (5760, 3240)
BACKGROUND = pygame.transform.scale(pygame.image.load('Assets/final-bg-empty.png'), BGSIZE)
CHAR_SPRITE1 = pygame.transform.smoothscale(pygame.image.load('Assets/dialogue_sprite1.png'), (500, 500))
CHAR_SPRITE2 = pygame.transform.smoothscale(pygame.image.load('Assets/dialogue_sprite2.png'), (500,500))
key_sprite = pygame.transform.smoothscale(pygame.image.load('Assets/key-icon.png'), (500, 500))
VARUN = pygame.transform.smoothscale(pygame.transform.flip(pygame.image.load('Assets/varun-agv.png'), True, False), (327.5, 595))
TRANSPARENT = pygame.image.load('Assets/transparent_image.png')
ITEM = pygame.image.load('Assets/item.png')
MUSIC = 'Assets/Celeste.mp3'