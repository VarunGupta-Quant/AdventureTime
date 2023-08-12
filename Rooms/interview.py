# Pygame CYOA
# Albert D, Varun G, Ivan W
# May 9, 2022
# Boss room

import pygame
import sys
from flower import rose_sprite as FLOWER
from friend import tie_sprite as TIE
from stranger import cloth_sprite as CLOTH
sys.path.insert(0, './')
from player import Object, Player
from dialogue import Dialogue
from reception import waterBottleItem as WATERBOTTLE
from inside import penIcon as PEN

def finish(player, objectList, screen, interface):  # Go to final menu if successful interview
    player.x = 600
    player.y = 500
    player.direction = 'D'
    return 'final_menu'

'''Interview has 5 questions
Some questions are not asked if the interviewee lacks certain items
Flower question has grayed out anser choice, but question is still asked
5 correct answers to win'''

def interview(player, objectList, screen, interface):
    correct_choices = 0
    text = Dialogue('times new roman', 32, 'WHITE', 
                    ['So you want to work for my company and you\'ve come here for an interview.',
                    'Say, why don\'t you tell me your name?',
                    'My name is Varun.',
                    'A pleasure to meet you Varun.',
                    'To start off the interview, I personally love to ask every preson I interview this question:',
                    'What is your greatest flaw??'],
                    ['Boss', 'Boss', 'Varun', 'Boss', 'Boss', 'Boss'],
                    [BOSS, BOSS, VARUN, BOSS, BOSS, BOSS],
                    voice = 'albert')
    text.play_dialogue(player, objectList, screen, interface)

    num, choice = text.display_choices(['I have no flaws.', 'I struggle with numbers.'], [True, True], player, objectList, screen, interface)
    if num == 0:
        text.dialogue = [choice,
                        'That\'s awesome! Our company, VaRoom, only accepts the top of the top.',
                        'Mistakes are not allowed in this environment.']
        text.characters = ['Varun', 'Boss', 'Boss']
        text.sprites = [VARUN, BOSS, BOSS]
        correct_choices += 1
    else:
        text.dialogue = [choice,
                        'So... you\'re saying that you\'re weak?', 
                        'Perhaps you aren\'t a perfect fit for us, after all...']
        text.characters = ['Varun', 'Boss', 'Boss']
        text.sprites = [VARUN, BOSS, BOSS]
    text.play_dialogue(player, objectList, screen, interface)

    if TIE in interface.items:
        text.dialogue = ['I didn\'t notice this before, but you\'re looking quite dapper there, Varun.', 'Why, thank you!']
        text.characters = ['Boss', 'Varun']
        text.sprites = [BOSS, VARUN]
        correct_choices += 1
        text.play_dialogue(player, objectList, screen, interface)
    
    text.dialogue = ['Man, I\'m feeling kind of thirsty right now, though...',
                     'You wouldn\'t happen to have some water, would you?']
    text.characters = ['Boss', 'Boss']
    text.sprites = [BOSS, BOSS]
    text.play_dialogue(player, objectList, screen, interface)
    
    if WATERBOTTLE in interface.items:
        text.dialogue = ['Yeah, I have a water bottle for you.',
                         'Oh wow, perftect! Let me get a sip real quick.',
                         'You\'re doing great so far, Varun! I\'m always impressed with those who come prepared for the job.']
        text.characters = ['Varun', 'Boss', 'Boss']
        text.sprites = [VARUN, BOSS, BOSS]
        correct_choices += 1
    else:
        text.dialogue = ['Sorry, I don\'t have a water bottle.',
                         'Hmmm... leaving me thirsty, eh?',
                         'Perhaps you aren\'t a perfect fit for us, after all...']
        text.characters = ['Varun', 'Boss', 'Boss']
        text.sprites = [VARUN, BOSS, BOSS]
    text.play_dialogue(player, objectList, screen, interface)

    text.dialogue = ['Here at our company, we look for someone who can think on their feet.',
                     'How would you describe yourself in one word?']
    text.characters = ['Boss', 'Boss']
    text.sprites = [BOSS, BOSS]
    text.play_dialogue(player, objectList, screen, interface)

    num, choice = text.display_choices(['My name is Varun', 'Chad'], [True, True], player, objectList, screen, interface)
    if num == 0:
        text.dialogue = [choice, 
                         'Hey, that\'s not one word...',
                         'Perhaps you aren\'t a perfect fit for us after all...',
                         'Anyway, I have a possible contract ready for you to sign. You just need to sign here-',
                         'Shoot! I forgot my pen...']
        text.characters = ['Varun', 'Boss', 'Boss', 'Boss', 'Boss']
        text.sprites = [VARUN, BOSS, BOSS, BOSS, BOSS]
    else:
        text.dialogue = [choice, 
                         'Wow, you followed my direction perfectly!',
                         'I think I\'m just about ready to have you join. Here, just sign this contract-',
                         'Shoot! I forgot my pen...']
        text.characters = ['Varun', 'Boss', 'Boss', 'Boss']
        text.sprites = [VARUN, BOSS, BOSS, BOSS]
        correct_choices += 1
    text.play_dialogue(player, objectList, screen, interface)

    if PEN in interface.items:
        text.dialogue = ['Amazing. Stellar. I\'m just about ready to hire you...']
        text.characters = ['Boss']
        text.sprites = [BOSS]
        correct_choices += 1
    else:
        text.dialogue = ['Hm… you don\'t have a pen, eh? Fine, then. Take my EXPO marker…']
        text.characters = ['Boss']
        text.sprites = [BOSS]
    text.play_dialogue(player, objectList, screen, interface)

    text.dialogue = ['And now… my final test for you. We value selflessness here at VaRoom.',
                     'Give me a present that would suit me best.']
    text.characters = ['Boss', 'Boss']
    text.sprites = [BOSS, BOSS]
    text.play_dialogue(player, objectList, screen, interface)

    num, choice = text.display_choices(['Nothing', 'Flower'], [True, FLOWER in interface.items], player, objectList, screen, interface)
    if num == 0:
        text.dialogue = [choice, 
                         'Wait, you don\'t have a gift for me?',
                         'A shame. I really like flowers.']
        text.characters = ['Varun', 'Boss', 'Boss']
        text.sprites = [VARUN, BOSS, BOSS]
        if CLOTH in interface.items:
            text.dialogue.append('well, I guess I\'ll take a washcloth. That\'s not bad either.')
            text.characters.append('Boss')
            text.sprites.append(BOSS)
            correct_choices += 1
    else:
        text.dialogue = [choice, 
                         'Oh, yippee, a flower! That\'s my favorite!']
        text.characters = ['Varun', 'Boss']
        text.sprites = [VARUN, BOSS]
        correct_choices += 1
    text.play_dialogue(player, objectList, screen, interface)

    if correct_choices >= 5:
        text.dialogue = ['Congratulations. You have passed my test. I think you are fit for the job.',
                         'Welcome to VaRoom, Varun!']
        text.characters = ['Boss', 'Boss']
        text.sprites = [BOSS, BOSS]
        finish(player, objectList, screen, interface)
    else:
        text.dialogue = ['Sorry, I don\'t think you\'re a good fit for our company.',
                         'Try again next time, Varun.']
        text.characters = ['Boss', 'Boss']
        text.sprites = [BOSS, BOSS]
    text.play_dialogue(player, objectList, screen, interface)
    return 'menu'

def sofaDialogue(player, objectList, screen, interface):
    text = Dialogue('times new roman', 32, 'WHITE', 
                    ['Wow, that\'s a comfy looking sofa.', 
                     'Varun sat in the sofa. It was comfy.'],
                    ['Varun', ''],
                    [VARUN, TRANSPARENT],
                    voice = 'albert')
    text.play_dialogue(player, objectList, screen, interface)

# Define objects

TRANSPARENT = pygame.image.load('Assets/transparent_image.png')
sofaRight = Object(1200,861, 103,200, 'Assets/transparent_image.png')
sofaLeft = Object(650, 862, 103, 200, 'Assets/transparent_image.png')
seatDown = Object(876,670, 220, 137, 'Assets/transparent_image.png', interview)
#seatRight = Object(2*493, 2*340, 2*102, 2*177, 'Assets/transparent_image.png')
#seatLeft = Object(2*126, 2*340, 2*102, 2*177, 'Assets/transparent_image.png')
seatUpper = Object(0,0,1920,635,'Assets/transparent_image.png')
boundaryLeft = Object(0,0,557,1078,'Assets/transparent_image.png')
boundaryRight = Object(1397,0,523,1080, 'Assets/transparent_image.png')
OBJECTLIST = [sofaRight, sofaLeft, seatDown, seatUpper, boundaryLeft,boundaryRight]
PLAYERDIRECTION = 'U'

# Characters and data for game

BGSIZE = (1920,1080)
MUSIC = 'Assets/Celeste.mp3'
BACKGROUND = pygame.transform.scale(pygame.image.load('Assets/backgrounds/boss-room.png'), (1920,1080))
BOSS = pygame.transform.scale(pygame.image.load('Assets/bob.png'), (300, 300))
VARUN = pygame.transform.smoothscale(pygame.transform.flip(pygame.image.load('Assets/varun-agv.png'), True, False), (327.5, 595))