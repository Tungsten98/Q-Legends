class GameMap:

    def __init__(self, gamedata):
        # Map dimensions
        self.dim = gamedata['map_dims']

        # "Grass" background colour
        self.backgorund_colour = gamedata['background_colour']

        # Tower positions (from centre)
        self.tower_pos_1 = gamedata['tower']['team_1_loc']
        self.tower_pos_2 = gamedata['tower']['team_2_loc']

        # Decorative "stone" tiles at tower areas
        self.stone_tile_colour = gamedata['stone_tile_colour']
        self.stone_tile_radius = gamedata['stone_tile_radius']
        # Clarify this position as origin of stone tiles
        self.stone_tile_circle_centres = (self.tower_pos_1, self.tower_pos_2)

        # Player spawn positions (from centre)
        self.player_spawn_pos_1 = gamedata['player']['team_1_spawn_loc']
        self.player_spawn_pos_2 = gamedata['player']['team_2_spawn_loc']

        # Minion nest positions (from centre)
        self.minion_nest_pos = gamedata['minion_nest']['loc']
        self.minion_h_spawn_pos = gamedata['minion']['h_spawn_loc']
        self.minion_v_spawn_pos = gamedata['minion']['v_spawn_loc']

        # Water (TODO: decide whether to move to separate class)
        self.water_colour = gamedata['water_colour']
        self.water_rect_len = gamedata['water_rect_len']
        self.water_rect_size = (self.water_rect_len, self.water_rect_len)
        self.water_map_len = gamedata['water_map_len']
        self.water_map = gamedata['water_map']
