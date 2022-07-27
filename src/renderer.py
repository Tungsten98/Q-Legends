import configparser, json
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
            self.screen.fill(game_map.backgorund_colour)

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
            for i in range(len(self.game_map.stone_tile_circle_centres)):
                pygame.draw.circle(self.screen, self.game_map.stone_tile_colour,
                                self.game_map.stone_tile_circle_centres[i],
                                self.game_map.stone_tile_radius)

            def draw_tower_pos(tower_pos):
                # Placeholders for towers
                tower_top_lefts = [j - 64 for j in tower_pos]
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
                                    (tower_top_lefts, (128, 128))
                                    )) # Tower placeholders
                tower_centres = [j - 8 for j in tower_pos]
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
                                    (tower_centres, (16, 16))
                                    )) # Tower centre markers

            draw_tower_pos(self.game_map.tower_pos_1)
            draw_tower_pos(self.game_map.tower_pos_2)

            # DEBUG: Draw the player spawn points
            def draw_player_spawn_pos(player_spawn_pos):
                for i in range(len(player_spawn_pos)):
                    pspawn_top_lefts = [j - 32 for j in player_spawn_pos[i]]
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
                                        (pspawn_top_lefts, (64, 64))
                                        )) # Player spawn placeholders
                    pspawn_centres = [j - 8 for j in player_spawn_pos[i]]
                    pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
                                        (pspawn_centres, (16, 16))
                                        )) # Player spawn centre markers

            draw_player_spawn_pos(self.game_map.player_spawn_pos_1)
            draw_player_spawn_pos(self.game_map.player_spawn_pos_2)

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
            for i in range(len(self.game_map.minion_v_spawn_pos)):
                mspawn_top_lefts = (self.game_map.minion_v_spawn_pos[i][0] - 4,
                                    self.game_map.minion_v_spawn_pos[i][1] - 8)
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
                                    (mspawn_top_lefts, (8, 16))
                                    )) # Minion spawn placeholders
                mspawn_centres = [j - 2 for j in self.game_map.minion_v_spawn_pos[i]]
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
                                    (mspawn_centres, (4, 4))
                                    )) # Minion spawn centre markers
            for i in range(len(self.game_map.minion_h_spawn_pos)):
                mspawn_top_lefts = (self.game_map.minion_h_spawn_pos[i][0] - 8,
                                    self.game_map.minion_h_spawn_pos[i][1] - 4)
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(
                                    (mspawn_top_lefts, (16, 8))
                                    )) # Minion spawn placeholders
                mspawn_centres = [j - 2 for j in self.game_map.minion_h_spawn_pos[i]]
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(
                                    (mspawn_centres, (4, 4))
                                    )) # Minion spawn centre markers

            # Flip (i.e. refresh) the display
            pygame.display.flip()

if __name__ == "__main__":
    game_config = configparser.ConfigParser()
    game_config.read("../config.ini") # TODO: change to absolute path
    with open(game_config['DATA']['GameDataFile'], 'r') as file:
        game_data = json.load(file)
    game_map = gamemap.GameMap(game_data)
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
