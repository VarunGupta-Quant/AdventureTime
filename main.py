# Pygame CYOA
# Albert D, Varun G, Ivan W
# May 9, 2022
# Run game


import sys
from dialogue import FONT, BOLD
from globals import *   

# import room variables
sys.path.insert(1, 'Rooms/')
import flower, friend, inside, interview, outside, stranger, reception

class Game:
    def __init__(self, game_state = 'menu'): 
        self.game_state = game_state

    def menu(self):
        while self.game_state == 'menu':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:                                # Click start button
                    if( screen.width/2 - 250 <= mouse[0] <= screen.width/2 + 250 and
                        screen.height/2 - 225 <= mouse[1] <= screen.height/2 - 25):
                        self.game_state = 'outside'
                        self.change_room()
                    elif(screen.width/2 - 250 <= mouse[0] <= screen.width/2 + 250 and   # Click Quit button
                        screen.height/2 + 25 <= mouse[1] <= screen.height/2 + 225):
                        sys.exit()
            
            screen.screen.blit(outside.BACKGROUND, (0,0))
            mouse = pygame.mouse.get_pos()
            
            # start button
            start = BOLD.render('START', True, 'WHITE')
            pygame.draw.rect(screen.screen, (100, 100, 100), pygame.Rect(screen.width/2 - 250, screen.height/2 - 225, 500, 200))
            screen.screen.blit(start, (screen.width/2 - start.get_width()/2, screen.height/2 - 125 - start.get_height()/2))

            # quit button
            quit = BOLD.render('QUIT', True, 'WHITE')
            pygame.draw.rect(screen.screen, (100, 100, 100), pygame.Rect(screen.width/2 - 250, screen.height/2 + 25, 500, 200))
            screen.screen.blit(quit, (screen.width/2 - quit.get_width()/2, screen.height/2 + 125 - quit.get_height()/2))

            pygame.display.update()

            pygame.time.Clock().tick(30)
    
    def change_room(self):
        global screen, objectList, player

        if(self.game_state != None):
            if(self.game_state == 'final_menu'):
                screen.fade = 'out'
                screen.background = pygame.transform.smoothscale(pygame.image.load('Assets/win.png'), (1920, 1080))
                BGSIZE = (1920, 1080)
                objectList = []
                self.play_game()
            else:
                if self.game_state == 'menu':
                    self.menu()
                screen.fade = 'out'
                screen.background = eval(self.game_state + '.BACKGROUND')
                screen.bg_size = eval(self.game_state + '.BGSIZE')
                
                objectList = eval(self.game_state + '.OBJECTLIST')
                
                pygame.mixer.music.load(eval(self.game_state + '.MUSIC'))
                pygame.mixer.music.set_volume(0.05)
                pygame.mixer.music.play(-1)
                self.play_game()

    def play_game(self): 
        global screen, player, objectList, interface, frame

        clock = pygame.time.Clock()

        while True:

            screen.refresh_screen(objectList, player, interface)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                # interaction keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:   
                        self.game_state = player.interact_object(objectList, screen, interface)
                        self.change_room()
                    
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    
                    # interface
                    if event.key == pygame.K_i:
                        interface.invStatus = not interface.invStatus
                        interface.mapStatus = False
                    if event.key == pygame.K_m:
                        interface.mapStatus = not interface.mapStatus      
                        interface.invStatus = False
                    
                    # speed up / down
                    if event.key == pygame.K_EQUALS:
                        player.speed = min(player.speed + 2, 20)
                    if event.key == pygame.K_MINUS:
                        player.speed = max(player.speed - 2, 2)

            # locks interaction in menu
            if interface.mapStatus or interface.invStatus:
                continue

            player.move(screen, objectList)
            
            frame += 1

            clock.tick(30)

if __name__ == '__main__':
    game = Game('menu')
    game.menu()