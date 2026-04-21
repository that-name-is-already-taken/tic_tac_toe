import pygame
from time import sleep


class GameUI:
    def __init__(self):
        self.screen = None  # Screen is initialized in self.display_window()
        self.screen_width, self.screen_height = 500, 500
        self.display_window()

        self.light_color = (211, 218, 217)
        self.dark_color = (68, 68, 78)
        self.display_board()

        pygame.display.flip()

    def display_window(self):
        """Creates self.screen object and sets window-related properties. """
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Tic-Tac-Toe by that-name-is-already-taken")
        icon = pygame.image.load("media/icon.png")
        pygame.display.set_icon(icon)

    def display_board(self):
        """Sets the background color and draws the lines. """
        self.screen.fill(self.dark_color)
        pygame.draw.line(self.screen, self.light_color, (200, 100), (200, 400), 2)
        pygame.draw.line(self.screen, self.light_color, (300, 100), (300, 400), 2)
        pygame.draw.line(self.screen, self.light_color, (100, 200), (400, 200), 2)
        pygame.draw.line(self.screen, self.light_color, (100, 300), (400, 300), 2)

    def display_winner_or_draw(self, player):
        """Displays the proper text after win or draw. """
        if player is None:
            self.format_text("DRAW")
        else:
            if player:
                self.format_text("CROSS WON")
            else:
                self.format_text("CIRCLE WON")

    def format_text(self, text):
        """Formats text appearing after the win or draw. """
        font = pygame.font.SysFont("arial", 28)

        text_surface = font.render(text, True, self.light_color)
        text_div = text_surface.get_rect(midtop=(self.screen_width // 2, 35))
        self.screen.blit(text_surface, text_div)

        pygame.display.flip()
        sleep(1)

    def display_xo(self, row, col, player):
        """Draws the proper symbol based on given row, column and player. """
        # Addition of 1 in case of x and y is needed due to offset caused by margins.
        if player:
            self.display_x(row + 1, col + 1)
        else:
            self.display_o(row + 1, col + 1)

    def display_x(self, row=0, col=0):
        """Draws cross based on given row and column. """
        x = col * 100
        y = row * 100
        pygame.draw.line(self.screen, self.light_color, (x + 20, y + 20), (x + 80, y + 80), 2)
        pygame.draw.line(self.screen, self.light_color, (x + 80, y + 20), (x + 20, y + 80), 2)

    def display_o(self, row=0, col=1):
        """Draws circle based on given row and column. """
        x = col * 100 + 50
        y = row * 100 + 50
        pygame.draw.circle(self.screen, self.light_color, (x, y), 35, 2)
