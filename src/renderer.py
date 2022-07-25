import pygame
import gamemap

# Initialise the pygame library
pygame.init()

class Renderer:
    def __init__(self, game_map, display=True):
        self.display = display
        self.game_map = game_map
        self.screen = None
        if self.display:
            self._init_screen()
            self.render_game_map()

    def _init_screen(self):
        self.screen = pygame.display.set_mode(self.game_map.dim)

    def render_game_map(self):
        if self.display:

            # Logic to update the game map with every sprite's
            # current position

            # Fill the background with the grass colour
            self.screen.fill(game_map.backgorund_colour_rgb)

            # Draw the towers and the decorative "stone" tiles underneath them
            for i in range(2):
                pygame.draw.circle(self.screen, self.game_map.stone_tile_colour,
                                self.game_map.stone_tile_circle_centres[i],
                                self.game_map.stone_tile_radius)

                # Placeholders for towers
                tower_top_lefts = [j - 64 for j in self.game_map.tower_pos[i]]
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
                                    (tower_top_lefts, (128, 128))
                                    )) # Tower placeholders
                tower_centres = [j - 8 for j in self.game_map.tower_pos[i]]
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
                                    (tower_centres, (16, 16))
                                    )) # Tower centre markers

            # Draw the minion nests
            for i in range(3):
                # Placeholders for minion nests
                tower_top_lefts = [j - 32 for j in self.game_map.minion_nest_pos[i]]
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
                                    (tower_top_lefts, (64, 64))
                                    )) # Minion nest placeholders
                tower_centres = [j - 8 for j in self.game_map.minion_nest_pos[i]]
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
                                    (tower_centres, (16, 16))
                                    )) # Nest centre markers

            # Flip (i.e. refresh) the display
            pygame.display.flip()

if __name__ == "__main__":
    game_map = gamemap.GameMap()
    renderer = Renderer(game_map, display=True)

    # Keep displaying the window until the user asks to quit
    running = True
    while running:

        for event in pygame.event.get():
            # User clicks the close button
            if event.type == pygame.QUIT:
                running = False

        renderer.render_game_map()

    pygame.quit()
