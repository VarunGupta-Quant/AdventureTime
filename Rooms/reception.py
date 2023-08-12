# Pygame CYOA
# Albert D, Varun G, Ivan W
# May 9, 2022
# Reception (before boss room)

import pygame
from player import Object, Player
import sys
sys.path.insert(0, './')

from player import Object, Player
from dialogue import Dialogue
import interface as mapInterface

'''Functions to enter different rooms (changes to instance variables are necessary
to specify location in new area)'''

def goBack(player, objectList, screen, interface):      # Corridor
    player.x = 4504.5+10
    player.y = 260
    player.direction = 'U'
    return 'inside'

def goInterview(player, objectList, screen, interface): # Boss room
    
    if len(interface.items) >= 5:
        player.x = 969
        player.y = 983
        return 'interview'
    else:                           # Room is locked until enoough items are obtained
        text = Dialogue('times new roman', 32, 'WHITE', ['You don\'t have enough items to enter this room yet...'
                                                         'Go back and find some more...'],
                        ['', ''], [TRANSPARENT, TRANSPARENT])
        text.play_dialogue(player, objectList, screen, interface)

def cabinetDialogue(player, objectList, screen, interface):
    text = Dialogue('times new roman', 32, 'WHITE',
                    ['I wonder if there\'s anything in this cabinet.',
                     'Varun pulled the cabinet open and found nothing.'],
                    ['Varun', ''],
                    [VARUN, TRANSPARENT])
    text.play_dialogue(player, objectList, screen, interface)

# def sofaDialogue(player, objectList, screen, interface):
#     text = Dialogue('times new roman', 32, 'WHITE',
#                 ['This is a nice looking sofa.']
#                 ['Varun'],
#                 [VARUN])
#     text.play_dialogue(player, objectList, screen, interface)

def potDialogue(player, objectList, screen, interface):         # Talk to Remy
    text = Dialogue('times new roman', 32, 'WHITE',
                    ['Woah... look at these cool pots!',
                     'Don\'t mind if I do... I\'m sure taking just one can\'t hurt...', 
                     'POT has been added to your inventory.'],
                    ['Varun', 'Varun', ''],
                    [VARUN, VARUN, TRANSPARENT])
    text.play_dialogue(player, objectList, screen, interface)
    interface.items.append(potItem)
    objectList.remove(pot)
    
def receptionDialogue(player, objectList, screen, interface):
    text = Dialogue('times new roman', 32, 'WHITE', 
                    ['Why, hello there!', 
                     'My name is Remy the Receptionist. I schedule all meetings for this workplace.', 
                     'You look like you have an appointment with me...', 
                     'May I ask what your name is?'], 
                     ['Receptionist', 'Receptionist', 'Receptionist', 'Receptionist'], 
                     [RECEPTIONIST, RECEPTIONIST, RECEPTIONIST, RECEPTIONIST])
    
    text.play_dialogue(player, objectList, screen, interface)
    num, choice = text.display_choices(['Varun.', 'No. You smell bad, Remy.'], [True, True], player, objectList, screen, interface)
    
    if num == 0:
        text.dialogue = [choice, 'Great! It seems like you don\'t have an appointment scheduled... I don\'t think-']
        text.characters = ['Varun', 'Receptionist']
        text.sprites = [VARUN, RECEPTIONIST]
        text.play_dialogue(player, objectList, screen, interface)
        
        num, choice = text.display_choices(['I\'ll bribe you.', 'Please! I need this!', 'I will destroy you.'],[True, True, True], player, objectList, screen, interface)
        if num == 0:
            text.dialogue = [choice, 'Excuse me? That is completely inappropriate!', 
                                'This establishment is known for its reputable status and ethical company policies.',
                                'How dare you! Go away!']
            text.characters = ['Varun', 'Receptionist', 'Receptionist', 'Receptionist']
            text.sprites = [VARUN, RECEPTIONIST, RECEPTIONIST, RECEPTIONIST]
            text.play_dialogue(player, objectList, screen, interface)
        elif num == 1:
            text.dialogue = [choice, 
                             'Young man, being desperate will get you nowhere in life.', 
                             'You are not ready to meet the Boss.']
            text.characters = ['Varun', 'Receptionist', 'Receptionist']
            text.sprites = [VARUN, RECEPTIONIST, RECEPTIONIST]
            text.play_dialogue(player,objectList, screen, interface)
        else:
            if potItem in interface.items: #change to if inventory contains pot
                text.dialogue = [choice, 
                                 'Good thing I picked up this POT not too long ago...',
                                 'OH MY GOODNESS! WHERE DID YOU GET THAT POT!',
                                 'PLEASE DON\'T SMASH THAT POT! IT\'S WORTH MILLIONS!',
                                 'FINE!!! I will schedule a meeting for you with the Boss.',
                                 'Here. Take this water bottle, and enter into the Boss\'s room. Have fun.', 'Water Bottle has been added to your inventory.']
                text.characters = ['Varun', 'Varun', 'Receptionist', 'Receptionist', 'Receptionist', 'Receptionist', '']
                text.sprites = [VARUN, VARUN, RECEPTIONIST, RECEPTIONIST, RECEPTIONIST, RECEPTIONIST, TRANSPARENT]
                text.play_dialogue(player, objectList, screen, interface)
                interface.items.append(waterBottleItem)
            else:
                text.dialogue = [choice, '...',
                                 'Are you threatening me?',
                                 'Please leave. This is not a joke.']
                text.characters = ['Varun', 'Receptionist', 'Receptionist', 'Receptionist']
                text.sprites = [VARUN, RECEPTIONIST, RECEPTIONIST, RECEPTIONIST]
                text.play_dialogue(player, objectList, screen, interface)
    else:
        text.dialogue = [ choice, 
                         'Well... that\'s not very nice of you, sir.', 
                         'Please go away before I call the police. I am going to go cry now.']
        
        
        text.characters = ['Varun', 'Receptionist', 'Receptionist']
        text.sprites = [VARUN, RECEPTIONIST, RECEPTIONIST]
        text.play_dialogue(player, objectList, screen, interface)
        
        
BACKGROUND = pygame.transform.scale(pygame.image.load('Assets/backgrounds/reception-1920.png'), (1920,1080))
MUSIC = 'Assets/Celeste.mp3'

boundary_shift = 540        # Offset boundaries because background image changed (centered the reception room)
mult_factor = 1.2

# Walls to constrain player movement
topWall = Object(boundary_shift,0,506*mult_factor,163*mult_factor, 'Assets/transparent_image.png', None)
leftWall = Object(boundary_shift,0,63*mult_factor,904*mult_factor, 'Assets/transparent_image.png', None)
rightWall = Object(boundary_shift+630*mult_factor,0,82*mult_factor,904*mult_factor,'Assets/transparent_image.png',None)
middleLedgeLeft = Object(boundary_shift,516*mult_factor,254*mult_factor,187*mult_factor, 'Assets/transparent_image.png', None)
middleLedgeRight = Object(boundary_shift+452*mult_factor,516*mult_factor,260*mult_factor,187*mult_factor, 'Assets/transparent_image.png', None)

exit = Object(boundary_shift+484*mult_factor,0,160*mult_factor, 40*mult_factor,'Assets/transparent_image.png', goBack)

# Items in reception area
potItem = pygame.transform.smoothscale(pygame.image.load('Assets/pot.png'), (500, 500))
waterBottleItem = pygame.transform.smoothscale(pygame.image.load('Assets/water-bottle.png'),(500,500))
cabinet = Object(boundary_shift+304*mult_factor,80*mult_factor,127*mult_factor,83*mult_factor, 'Assets/transparent_image.png', cabinetDialogue)
table = Object(boundary_shift+484*mult_factor,361*mult_factor,151*mult_factor,151*mult_factor, 'Assets/transparent_image.png')
pot = Object(boundary_shift+480*mult_factor, 418*mult_factor, 50*mult_factor,60*mult_factor, 'Assets/transparent_image.png', potDialogue)
receptionDesk = Object(boundary_shift,0,251*mult_factor,270*mult_factor,'Assets/transparent_image.png',receptionDialogue)
stairs = Object(boundary_shift+493*mult_factor,64*mult_factor,152*mult_factor,140*mult_factor,'Assets/transparent_image.png', goInterview)

backToCorridor = Object(0,1070,1920,60,'Assets/transparent_image.png', goBack)
OBJECTLIST = [cabinet, pot, table, receptionDesk, exit, backToCorridor, stairs, topWall, leftWall, rightWall, middleLedgeLeft, middleLedgeRight]
POSX = boundary_shift+558*1.2
POSY = 50*mult_factor
PLAYERDIRECTION = 'U'
TRANSPARENT = pygame.image.load('Assets/transparent_image.png')
BGSIZE = (1920,1080)
RECEPTIONIST = pygame.transform.smoothscale(pygame.image.load('Assets/receptionist-remy.png'), (500, 500))
VARUN = pygame.transform.smoothscale(pygame.transform.flip(pygame.image.load('Assets/varun-agv.png'), True, False), (327.5, 595))