import pygame
from game.game_logic import GameLogic
from game.game_ui import GameUI


def main():
    """Main Game-Loop is responsible for the proper handling of GameLogic() and GameUI(). """
    gl = GameLogic()
    gui = GameUI()

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                result = gl.click_action(pygame.mouse.get_pos())

                if result is not None:
                    gui.display_xo(*result)
                    winner = gl.check_win()

                    if winner is not None or gl.check_full_board():
                        gui.display_winner_or_draw(winner)
                        gui.display_board()
                        gl.clear_board()

        pygame.display.flip()


if __name__ == "__main__":
    main()
