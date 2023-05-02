import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Ogólna klasa di zarządzania zasobami i sposobem dzialania gry"""
    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.scree_height))
        pygame.display.set_caption("Alien Invasion")

        #Definiowanie koloru
        self.bg_color = (self.settings.bg_color)
        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Rekcja na klawiaturę i myszkę"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    #Utworzenie egzemplarza gry i jej uruchomienie.
    ai = AlienInvasion()
    ai.run_game()