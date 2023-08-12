# Pygame CYOA
# Albert D, Varun G, Ivan W
# May 9, 2022
# Dialogue for game sprites and character interactions

from audio import factor_sentence
import pygame
import sys
pygame.init()

TEXTBOX = pygame.image.load('Assets/textbox.png')     # textbox image
WIDTH = TEXTBOX.get_width()                             # textbox width
HEIGHT = TEXTBOX.get_height()                           # textbox height
FONT = pygame.font.SysFont('times new roman', 32)       # pygame font
BOLD = pygame.font.SysFont('times new roman', 50, True)

def multiLineSurface(string, font, rect, fontColour, surface, offset=100):
    """Returns a surface containing the passed text string, reformatted
    to fit within the given rect, word-wrapping as necessary. The text
    will be anti-aliased.

    Parameters
    ----------
    string - the text you wish to render. \n begins a new line.
    font - a Font object
    rect - a rect style giving the size of the surface requested.
    fontColour - a three-byte tuple of the rgb value of the
            text color. ex (0, 0, 0) = BLACK
    surface - textbox surface that you wish to paste the text on

    Returns
    -------
    Success - a surface object with the text rendered onto it.
    Failure - raises a TextRectException if the text won't fit onto the surface.
    """

    finalLines = []
    requestedLines = string.splitlines()
    # Create a series of lines that will fit on the provided
    # rectangle.
    for requestedLine in requestedLines:
        if font.size(requestedLine)[0] > rect.width:
            words = requestedLine.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise TextRectException("The word " + word + " is too long to fit in the rect passed.")
            # Start a new line
            accumulatedLine = ""
            for word in words:
                testLine = accumulatedLine + word + " "
                # Build the line while the words fit.
                if font.size(testLine)[0] < rect.width:
                    accumulatedLine = testLine
                else:
                    finalLines.append(accumulatedLine)
                    accumulatedLine = word + " "
            finalLines.append(accumulatedLine)
        else:
            finalLines.append(requestedLine)

    # Let's try to write the text out on the surface.
    accumulatedHeight = 0
    for line in finalLines:
        if accumulatedHeight + font.size(line)[1] >= rect.height - offset:
            raise TextRectException("Once word-wrapped, the text string was too tall to fit in the rect.")
        if line != "":
            tempSurface = font.render(line, 1, fontColour)
        surface.blit(tempSurface, ((surface.get_width() - tempSurface.get_width()) / 2, accumulatedHeight + offset))
        accumulatedHeight += font.size(line)[1]
    return surface

class Dialogue(): 
    def __init__(self, font, size, color, dialogue, characters, sprites, BGColor = 'BLACK', borderColor = 'WHITE', voice = 'ivan', pitch = 1):
        self.font = pygame.font.SysFont(font, size)     # pygame font
        self.color = pygame.Color(color)                # pygame color
        self.dialogue = dialogue                        # dialogue list
        self.characters = characters                    # character name list
        self.sprites = sprites                          # pygame sprite list
        self.BGColor = BGColor                          # textbox background color
        self.borderColor = borderColor                  # textbox border color
        self.voice = voice                              # select voice to use
        self.pitch = pitch                              # multiplier of voiceline speed / pitch

    def draw_textbox(self, screen): 
        # Creates textbox surface to paste on
        textbox_surface = pygame.Surface((screen.width - 300, 300))
        textbox_surface.fill(self.borderColor)
        textbox_surface.fill(self.BGColor, textbox_surface.get_rect().inflate(-10, -10))
        return textbox_surface

    def text_animation(self, index, loc, player, objectList, screen, interface):
        # Plays text character-by-character
        text = ''
        j = 0

        while j < len(self.dialogue[index]):
            screen.render_background()
            screen.render_objects(objectList, player)
            screen.render_ui(interface)

            # skip to end on SPACE or MOUSEBUTTONDOWN
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT:
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    text = self.dialogue[index][:-1]                                        # add characters except for last
                    j = len(self.dialogue[index]) - 1                                       # largest possible value of j

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        text = self.dialogue[index][:-1]                                    # add characters except for last
                        j = len(self.dialogue[index]) - 1                                   # largest possible value of j
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            textbox_surface = self.draw_textbox(screen)                                           # draw textbox on screen
            self.draw_sprite(self.sprites[index], loc, screen)                      # draw character sprite
            self.draw_name(self.characters[index], loc, textbox_surface)                                   # draw character name on textbox

            # ADDING CHARACTER TO TEXT
            text += self.dialogue[index][j]                                                 # add next character to text
            multiLineSurface(text, FONT, pygame.Rect(0, 0, screen.width - 600, 300), 'WHITE', textbox_surface)# self.font.render(text, True, self.color)             # render new text
            screen.screen.blit(textbox_surface, (150, screen.height - 300))      # paste new text on textbox
            
            pygame.display.update()
            j += 1                                                              # increment index variable

    def draw_sprite(self, sprite, loc, screen):
        # draw character sprites on screen
        if loc: # display on left side of screen
            screen.screen.blit(sprite, (150, screen.height - 300 - sprite.get_height()))
        else:   # display on right side of screen
            screen.screen.blit(sprite, (screen.width - sprite.get_width() - 150, screen.height - 300 - sprite.get_height()))

    def draw_name(self, char, loc, surface):
        # render character name on textbox_surface
        name = BOLD.render(char, True, self.color)
        
        if loc: 
            # display on left side of screen
            surface.blit(name, (50, 25))
        else:   
            # display on right side of screen
            surface.blit(name, (surface.get_width() - 50 - name.get_width(), 25))

    def play_dialogue(self, player, objectList, screen, interface):
        
        for i in range(len(self.dialogue)):                                             # iterate through each piece of dialogue

            loc = (self.characters[i] == 'Varun')                            # determine sprite / name location

            factor_sentence(self.dialogue[i], self.voice, self.pitch)                                           # create voiceline for dialogue and export to output.wav
            sound = pygame.mixer.Sound('output.wav')                                    # load output.wav into pygame mixer
            pygame.mixer.Sound.play(sound)                                              # play dialogue

            self.text_animation(i, loc, player, objectList, screen, interface)      # play text animation

            pygame.event.clear()                                                        # clear event cache
            
            while True:                                                                 # hold end-of-dialogue state
                event = pygame.event.wait()                                             # wait until an event occurs
                
                if event.type == pygame.QUIT:
                    sys.exit()                                                          # QUIT               
                    
                if event.type == pygame.MOUSEBUTTONDOWN:                                # proceed on MOUSEBUTTONDOWN
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:                                     # proceed on SPACE
                        break
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()                                                      # QUIT
            
            pygame.mixer.Sound.stop(sound)                                              # terminate any voicelines currently playing
            
    def display_choices(self, choices, bool_choices, player, objectList, screen, interface):
        # Display choices to select from
        selection = bool_choices.index(True)        # first selectable choice
        frame = 0                                   # frame for border animation
        inc = 1                                     # frame increment

        while True:    
            screen.render_background()
            screen.render_objects(objectList, player)
            screen.render_ui(interface)

            for index in range(len(choices)): 
                button_rect = pygame.Rect(0, 0, 500, 150)
                button_surface = pygame.Surface((500, 150))
                button_surface.fill((100, 100, 100))
                if bool_choices[index]:
                    multiLineSurface(choices[index], self.font, button_rect, self.color, button_surface, 59)
                else:
                    multiLineSurface(choices[index], self.font, button_rect, (150, 150, 150), button_surface, 59)
                screen.screen.blit(button_surface, (screen.width/2 - 250, screen.height/2 - (index/2) * 300))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        selection = (selection + 1) % len(choices)
                        while not bool_choices[selection]:
                            selection = (selection + 1) % len(choices)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_d:
                        selection = (selection - 1) % len(choices)
                        while not bool_choices[selection]:
                            selection = (selection - 1) % len(choices)
                    elif event.key == pygame.K_RETURN:
                        return selection, choices[selection] 
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit()

            pygame.draw.rect(screen.screen, 
                             (100 + frame * 2, 100 + frame * 2, 100 + frame * 2), 
                             pygame.Rect(screen.width/2 - 250, 
                                         screen.height/2 - (selection/2) * 300,
                                         500, 
                                         150), 
                            5)

            if frame == 0:
                inc = 1
            elif frame == 60:
                inc = -1
            frame += inc

            pygame.display.update()
            pygame.time.Clock().tick(30)