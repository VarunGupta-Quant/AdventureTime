# Pygame CYOA
# Albert D, Varun G, Ivan W
# May 9, 2022
# Screen display

import pygame

class Screen: 
    def __init__(self, background, bg_size, x, y, width, height, fade = None):
        self.bg_size = bg_size                                              # background size
        self.background = pygame.transform.scale(background, self.bg_size)  # screen background
        self.x = x                                                          # x position of camera
        self.y = y                                                          # y position of camera
        self.width = width                                                  # screen width
        self.height = height                                                # screen height
        self.screen = pygame.display.set_mode((width, height))              # screen surface
        self.alpha = 0                                                  # alpha value overlay
        self.alphaSurface = pygame.Surface((self.width, self.height))                    # alpha surface overlay
        self.alphaSurface.fill((0,0,0))                                     # alphasurface = black
        self.fade = fade                                                    # bool for fading status

    def scroll(self, player):
        # align camera x-position according to player
        if(player.x <= self.x + self.width * .45):
            self.x = max(player.x - self.width * .45, 0)
        elif(player.x >= self.x + self.width * .55):
            self.x = min(player.x - self.width * .55, self.bg_size[0] - self.width)

        # align camera y-position according to player
        if(player.y <= self.y + self.height * .45):
            self.y = max(player.y - self.height * .45, 0)
        elif(player.y >= self.y + self.height * .55):
            self.y = min(player.y - self.height * .55, self.bg_size[1]  - self.height)

    def render_objects(self, objectList, player): 
        blitList = objectList.copy()
        blitList.append(player)
        blitList.sort(key = lambda obj: obj.y)
        player_index = blitList.index(player)

        for i in range(len(blitList)):
            if i == player_index:
                self.screen.blit(player.sprite, (player.x - self.x - 25, player.y - self.y - 75))
            else:
                self.screen.blit(blitList[i].sprite, (blitList[i].x - self.x, blitList[i].y - self.y)) 

    def render_background(self): 
        # render background
        self.screen.blit(self.background, (-self.x, -self.y))

    def render_ui(self, interface):
        # render user interface
        interface.open_map(self)
        interface.open_inventory(self)

    def refresh_screen(self, objectList, player, interface): 
        self.scroll(player)
        
        if self.fade == 'out':            
            # slowly increase alphaSurface opacity
            self.alphaSurface.set_alpha(self.alpha)
            self.screen.blit(self.alphaSurface, (0,0))
            self.alpha += 8
            
            # end of fade animation
            if self.alpha >= 255:
                self.fade = 'in'
       
        elif self.fade == 'in':
            self.render_background()
            self.render_objects(objectList, player)
            self.render_ui(interface)

            # slowly decrease alphaSurface opacity
            self.alphaSurface.set_alpha(self.alpha)
            self.screen.blit(self.alphaSurface, (0,0))
            self.alpha -= 8
            if self.alpha <= 0:
                self.fade = None

        else:
            # normal refresh screen
            self.render_background()
            self.render_objects(objectList, player)
            self.render_ui(interface)

        pygame.display.update()