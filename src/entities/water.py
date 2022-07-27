import pygame
from pygame.sprite import Sprite

class Water(Sprite):
    def __init__(self, pos, water_rect_len, water_colour):
        super(Water, self).__init__()
        self.dims = (water_rect_len, water_rect_len)
        self.surf = pygame.Surface(self.dims)
        self.surf.fill(water_colour)
        self.rect = self.surf.get_rect(topleft=pos)

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
