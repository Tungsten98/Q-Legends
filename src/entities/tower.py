import pygame
from pygame.sprite import Sprite

class Tower(Sprite):
    def __init__(self, pos):
        super(Tower, self).__init__()
        self.dims = (128, 128)
        self.surf = pygame.Surface(self.dims)
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=pos)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
