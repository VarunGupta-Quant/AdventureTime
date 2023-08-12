# Pygame CYOA
# Albert D, Varun G, Ivan W
# May 9, 2022
# Objects and player

import pygame
from dialogue import Dialogue

class Player:
    def __init__(self, x, y, width, height, sprite, speed, scale = 1): 
        self.x = x                      # x-coordinate
        self.y = y                      # y-coordinate
        self.width = width              # collision width
        self.height = height            # collision height
        self.sprite = pygame.transform.scale(pygame.image.load(sprite), (width, height))            # sprite
        self.speed = speed              # speed
        self.direction = 'U'            # direction facing
        self.idle_cycle = 0             # idle cycle index
        self.walk_cycle = 0             # walk cycle index
        self.scale = scale              # scale of sprite

    def change_direction(self):
            # records keys continually pressed
            keys = pygame.key.get_pressed()

            # WASD, Arrow Key Directions
            horizontal_move = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])
            vertical_move = (keys[pygame.K_DOWN] or keys[pygame.K_s]) - (keys[pygame.K_UP] or keys[pygame.K_w])
            
            # change direction of player
            if horizontal_move > 0: 
                self.direction = 'R'
            elif horizontal_move < 0: 
                self.direction = 'L'
            if vertical_move > 0: 
                self.direction = 'D'
            elif vertical_move < 0:
                self.direction = 'U'

            return horizontal_move, vertical_move

    def sprite_cycle(self, horizontal_move, vertical_move):
        # play idle animation
        if horizontal_move == 0 and vertical_move == 0:
            self.sprite = pygame.transform.scale(pygame.image.load('Assets/Varun/' + self.direction + '_idle/' + str((int)((self.idle_cycle - self.idle_cycle%36)/36 + 1)) + '.png'), (100*self.scale,100*self.scale))
            self.idle_cycle = (1 + self.idle_cycle) % 72      # through only first 2 frames
            self.walk_cycle = 0                               # reset walk cycle
        # play walk animation
        else: 
            self.sprite = pygame.transform.scale(pygame.image.load('Assets/Varun/' + self.direction + '_moving/' + str((int)((self.walk_cycle - self.walk_cycle%2)/2 + 1)) + '.png'), (100*self.scale,100*self.scale))
            self.walk_cycle = (1 + self.walk_cycle) % 16      # through 8 walk_cycle frames
            self.idle_cycle = 0                               # reset idle cycle

    def move(self, screen, objectList):
            # obtain user-inputted directional movement
            horizontal_move, vertical_move = self.change_direction()

            # move player horizontally according to keys pressed
            self.x += self.speed * horizontal_move
            
            if self.detect_collision(objectList) or (self.x - screen.x <= 0) or (self.x - screen.x >= screen.width): 
                # undo movement if collision
                self.x -= self.speed * horizontal_move
            
            # move player vertically according to keys pressed
            self.y += self.speed * vertical_move
            
            if self.detect_collision(objectList) or (self.y - screen.y <= 0) or (self.y - screen.y >= screen.height):
                # undo movement if collision
                self.y -= self.speed * vertical_move 
            
            # change player sprite based and idle / walk cycle
            self.sprite_cycle(horizontal_move, vertical_move)

    def detect_collision(self, objectList): 
        # iterate through all objects on screen
        for object in objectList:
            # check if width collision of object and player intersect
            if (object.x >= self.x and object.x < self.x + self.width) or (self.x >= object.x and self.x < object.x + object.width): 
                # check if height collision of object and player interesect
                if (object.y >= self.y and object.y < self.y + self.height) or (self.y >= object.y and self.y < object.y + object.height):      
                    return object
        return False

    def interact_object(self, objectList, screen, interface):
        # check movement based on direction
        horizontal = 50 * ( (int)(self.direction == 'R') - (int)(self.direction == 'L') )
        vertical = 50 * ( (int)(self.direction == 'D') - (int)(self.direction == 'U') )
        
        # move player 50 units in current direction
        self.y += vertical
        self.x += horizontal

        # check for collision
        if other := self.detect_collision(objectList):
            self.y -= vertical
            self.x -= horizontal
            return other.interact(self, objectList, screen, interface)
        
        # return player to original position
        self.y -= vertical
        self.x -= horizontal

class Object(Player):
    def __init__(self, x, y, width, height, sprite, prompt = None):
        super().__init__(x, y, width, height, sprite, speed = 0)
        self.prompt = prompt        # dialogue prompt

    def interact(self, player, objectList, screen, interface):
        # play dialogue
        if isinstance(self.prompt, Dialogue):
            self.prompt.play_dialogue(player, objectList, screen, interface)
        
        elif callable(self.prompt):
            return self.prompt(player, objectList, screen, interface)

        # do nothing
        return None