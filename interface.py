# Pygame CYOA
# Albert D, Varun G, Ivan W
# May 9, 2022
# Map and inventory

import pygame

BOX_WIDTH = 200             # grid box width
BOX_HEIGHT = 200            # grid box height
BOX_RADIUS = 30             # grid box corner radius
BOX_COLOR = (179,139,109)   # grid box color
MAP = pygame.image.load('Assets/varun-map.png')

class Interface():
    def __init__(self, inventory, items, invStatus = False, mapStatus = False):
        self.inventory = pygame.image.load(inventory)       # inventory image
        self.items = items                                  # item image list
        self.invStatus = invStatus                          # bool value on opening the inventory
        self.mapStatus = mapStatus                          # bool value on opening the map
    
    def draw_grid(self, screen):
        # draw inventory grid on screen
        
        x_space = screen.width % BOX_WIDTH                          # horizontal space between boxes
        x_boxes = (int)( (screen.width - x_space) / BOX_WIDTH )     # number of boxes in row
        y_space = screen.height % BOX_HEIGHT                        # vertical space between boxes
        y_boxes = (int)( (screen.height - y_space) / BOX_HEIGHT )   # number of boxes in column
        
        for x in range(1, x_boxes + 1):
            for y in range(1, y_boxes + 1):
                # draw grid box
                rect = pygame.Rect( (BOX_WIDTH + x_space / (x_boxes + 1) ) * x - BOX_WIDTH,         # x-coordinate 
                                    (BOX_HEIGHT + y_space / (y_boxes + 1) ) * y - BOX_HEIGHT,       # y-coordinate
                                    BOX_WIDTH,                                                      # width
                                    BOX_HEIGHT)                                                     # height
                pygame.draw.rect(screen.screen, BOX_COLOR, rect, 0, BOX_RADIUS)
                
                # draw item in grid box
                if((y-1) * x_boxes + x <= len(self.items)):
                    screen.screen.blit( pygame.transform.scale(self.items[(y-1) * x_boxes + x - 1], (BOX_WIDTH, BOX_HEIGHT) ), 
                                        ((BOX_WIDTH + x_space / (x_boxes + 1) ) * x - BOX_WIDTH,    # x-coordinate
                                        (BOX_HEIGHT + y_space / (y_boxes + 1) ) * y - BOX_HEIGHT)) # y-coordinate

    def open_map(self, screen):
        if(self.mapStatus):
            screen.screen.blit(pygame.transform.smoothscale(MAP, (screen.width, screen.height)), (0, 0))
            # draw objects and player location on map

    def open_inventory(self, screen):
        if(self.invStatus):
            # draw inventory image
            screen.screen.blit(pygame.transform.smoothscale(self.inventory, (screen.width, screen.height)), (0, 0))
            # draw inventory grid
            self.draw_grid(screen)