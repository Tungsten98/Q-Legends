import pygame
from pygame.sprite import Sprite

class MinionNest(Sprite):
    def __init__(self, pos):
        super(MinionNest, self).__init__()
        self.dims = (64, 64)
        self.surf = pygame.Surface(self.dims)
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=pos)
        # Store pos as this is needed to determine minion spawn positions
        self.pos = pos

    def get_minion_spawn_params(self):
        return [((self.pos[0] - 48, self.pos[1] - 8), True, self), # Left-top
                ((self.pos[0] - 48, self.pos[1] + 8), True, self), # Left-bottom
                ((self.pos[0] + 48, self.pos[1] - 8), True, self), # Right-top
                ((self.pos[0] + 48, self.pos[1] + 8), True, self), # Right-bottom
                ((self.pos[0] - 8, self.pos[1] - 48), False, self), # Top-left
                ((self.pos[0] - 8, self.pos[1] + 48), False, self), # Bottom-left
                ((self.pos[0] + 8, self.pos[1] - 48), False, self), # Top-right
                ((self.pos[0] + 8, self.pos[1] + 48), False, self)] # Bottom-right

    def draw(self, screen):
        screen.blit(self.surf, self.rect)
