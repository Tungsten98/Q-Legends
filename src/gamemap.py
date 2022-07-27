from entities.minion import Minion
from entities.minion_nest import MinionNest
from entities.tower import Tower
from entities.player import Player
from entities.water import Water

class GameMap:

    def __init__(self, gamedata):
        # Map dimensions
        self.dim = gamedata['map_dims']

        # "Grass" background colour
        self.backgorund_colour = gamedata['background_colour']

        # Tower positions (from centre)
        self.tower_pos_1 = gamedata['tower']['team_1_loc']
        self.tower_pos_2 = gamedata['tower']['team_2_loc']
        self.towers = [Tower(self.tower_pos_1), Tower(self.tower_pos_2)]

        # Decorative "stone" tiles at tower areas
        self.stone_tile_colour = gamedata['stone_tile_colour']
        self.stone_tile_radius = gamedata['stone_tile_radius']
        # Clarify this position as origin of stone tiles
        self.stone_tile_circle_centres = (self.tower_pos_1, self.tower_pos_2)

        # Player spawn positions (from centre)
        self.player_spawn_pos_1 = gamedata['player']['team_1_spawn_loc']
        self.player_spawn_pos_2 = gamedata['player']['team_2_spawn_loc']
        self.players = [[Player(pos) for pos in self.player_spawn_pos_1],
                        [Player(pos) for pos in self.player_spawn_pos_2]]

        # Minion nest positions (from centre)
        self.minion_nest_pos = gamedata['minion_nest']['loc']
        self.minion_nests = [MinionNest(pos) for pos in self.minion_nest_pos]
        minion_params = [nest.get_minion_spawn_params() \
                         for nest in self.minion_nests]
        self.minions = [[Minion(*params) for params in param_set] \
                        for param_set in minion_params]

        # Water
        self.water_colour = gamedata['water_colour']
        self.water_rect_len = gamedata['water_rect_len']
        self.water_map_len = gamedata['water_map_len']
        self.water_map = gamedata['water_map']
        self.water_bodies = [
            Water((j * self.water_rect_len,
                   i * self.water_rect_len),
                   self.water_rect_len, self.water_colour)
            for i in range(self.water_map_len)
            for j in range(self.water_map_len)
            if self.water_map[i][j] == 1
        ]
