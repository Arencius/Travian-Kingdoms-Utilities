import tkpy
import math
from data.user_data import DRIVER
from .finder import Finder


class ElephantFinder(Finder):
    """
    Class used to find elephants in the oases.
    """

    def __init__(self, village_name):
        super().__init__(village_name)

        game_map = tkpy.Map(DRIVER)
        game_map.pull()

        oases = game_map.gen_unoccupied_oases()
        self.oases_filtered = filter(lambda x: x.coordinate.x > 0 and x.coordinate.y > 0, oases)

    def distance(self, oasis_coords):
        return super().distance(oasis_coords)

    def find(self):
        for o in self.oases_filtered:
            units = o.req_details().get('troops')['units']
            if isinstance(units, dict) and '10' in units.keys():  # elephants have the value '10' in troops dictionary
                oasis_coords = o.coordinate.x, o.coordinate.y
                yield oasis_coords

    def closest_elephants(self, oases):
        super().closest(oases)