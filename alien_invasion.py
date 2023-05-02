import sys
import pygame


class AlienInvasion:
    """Ogólna klasa di zarządzania zasobami i sposobem dzialania gry"""
    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    #Utworzenie egzemplarza gry i jej uruchomienie.
    ai = AlienInvasion()
    ai.run_game()