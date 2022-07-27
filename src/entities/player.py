import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, pos):
        super(Player, self).__init__()
        self.dims = (64, 64)
        self.surf = pygame.Surface(self.dims)
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=pos)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
