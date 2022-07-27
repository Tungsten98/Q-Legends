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
            for water in self.game_map.water_bodies:
                water.draw(self.screen)
            
            # Draw the towers and the decorative "stone" tiles underneath them
            for i in range(len(self.game_map.stone_tile_circle_centres)):
                pygame.draw.circle(self.screen, self.game_map.stone_tile_colour,
                                self.game_map.stone_tile_circle_centres[i],
                                self.game_map.stone_tile_radius)

            # Draw entity sprites
            for tower in self.game_map.towers:
                tower.draw(self.screen)

            for player_group in self.game_map.players:
                for player in player_group:
                    player.draw(self.screen)

            for nest in self.game_map.minion_nests:
                nest.draw(self.screen)

            for minion_nest_group in self.game_map.minions:
                for minion in minion_nest_group:
                    minion.draw(self.screen)

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
