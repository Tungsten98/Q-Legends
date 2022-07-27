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

            # Draw the bodies of water
            for i in range(self.game_map.water_map_len):
                for j in range(self.game_map.water_map_len):
                    if self.game_map.water_map[i][j] == 1:
                        pygame.draw.rect(self.screen, self.game_map.water_colour,
                                        pygame.Rect(
                                        ((j * self.game_map.water_rect_len,
                                          i * self.game_map.water_rect_len),
                                          self.game_map.water_rect_size)
                                        ))

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

            # DEBUG: Draw the player spawn points
            for i in range(len(self.game_map.player_spawn_pos)):
                for j in range(len(self.game_map.player_spawn_pos[i])):
                    pspawn_top_lefts = [k - 32 for k in self.game_map.player_spawn_pos[i][j]]
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
                                        (pspawn_top_lefts, (64, 64))
                                        )) # Player spawn placeholders
                    pspawn_centres = [k - 8 for k in self.game_map.player_spawn_pos[i][j]]
                    pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
                                        (pspawn_centres, (16, 16))
                                        )) # Player spawn centre markers

            # Draw the minion nests
            for i in range(len(self.game_map.minion_nest_pos)):
                tower_top_lefts = [j - 32 for j in self.game_map.minion_nest_pos[i]]
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
                                    (tower_top_lefts, (64, 64))
                                    )) # Minion nest placeholders
                tower_centres = [j - 8 for j in self.game_map.minion_nest_pos[i]]
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
                                    (tower_centres, (16, 16))
                                    )) # Nest centre markers

            # DEBUG: Draw the minion spawn points
            for i in range(len(self.game_map.minion_spawn_pos[0])):
                mspawn_top_lefts = (self.game_map.minion_spawn_pos[0][i][0] - 4,
                                    self.game_map.minion_spawn_pos[0][i][1] - 8)
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
                                    (mspawn_top_lefts, (8, 16))
                                    )) # Minion spawn placeholders
                mspawn_centres = [j - 2 for j in self.game_map.minion_spawn_pos[0][i]]
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
                                    (mspawn_centres, (4, 4))
                                    )) # Minion spawn centre markers
            for i in range(len(self.game_map.minion_spawn_pos[1])):
                mspawn_top_lefts = (self.game_map.minion_spawn_pos[1][i][0] - 8,
                                    self.game_map.minion_spawn_pos[1][i][1] - 4)
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
                                    (mspawn_top_lefts, (16, 8))
                                    )) # Minion spawn placeholders
                mspawn_centres = [j - 2 for j in self.game_map.minion_spawn_pos[1][i]]
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
                                    (mspawn_centres, (4, 4))
                                    )) # Minion spawn centre markers

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
