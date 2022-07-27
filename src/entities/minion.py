import pygame
from pygame.sprite import Sprite

class Minion(Sprite):
    def __init__(self, pos, is_horizontal, nest):
        super(Minion, self).__init__()
        self.dims = (16, 8) if is_horizontal else (8, 16)
        self.surf = pygame.Surface(self.dims)
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=pos)

        self.nest = nest

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
