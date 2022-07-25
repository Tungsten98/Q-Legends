class GameMap:

    def __init__(self):
        # Map dimensions
        self.dim = (768, 768)

        # "Grass" background colour
        self.backgorund_colour_rgb = (7, 93, 2)

        # Tower positions (from centre): (T1, T2)
        # Top-left corners: ((16, 624), (624, 16)), + 1/2 * tower size
        self.tower_pos = ((80, 688), (688, 80))

        # Decorative "stone" tiles at tower areas
        self.stone_tile_colour = (228, 211, 204)
        self.stone_tile_radius = 164 # experiment
        # Clarify this position as origin of stone tiles
        self.stone_tile_circle_centres = self.tower_pos

        # Minion nest positions
        # Top-left corners: ((80, 80), (352, 352), (624, 624)), + 1/2 * nest size
        self.minion_nest_pos = ((112, 112), (384, 384), (656, 656))
