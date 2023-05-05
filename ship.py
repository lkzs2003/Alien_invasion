import pygame


class Ship:
    """Klasa przeznaczona do zarządzania statkiem kosmicznym"""

    def __init__(self, ai_game):
        """Inicjalizacja statku kosmicznego i jego położenie początkowe"""

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Wczytywanie statku kosmicznego i pobranie jego prostokąta
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Każdy nowy statek pojawia się na dole ekranu
        self.rect.midbottom = self.screen_rect.midbottom

        # Położenie poziomu staktu (typ float)
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Uaktualnienie obiectu rect na podstawie wartości self.x
        self.rect.x = self.x

    def blitme(self):
        """Wyświetlanie statku w jego akutalnym położeniu"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)