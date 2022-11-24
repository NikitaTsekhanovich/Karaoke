import pygame


class Background():
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.sprites = pygame.transform.scale(pygame.image.load("karaoke.jpg"), [480, 416])
        self.image = self.sprites.subsurface(0, 0,  480, 416)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)
