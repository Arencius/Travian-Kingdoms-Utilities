import tkpy
import math
from data.user_data import DRIVER


def get_quarter(coords):
    """
    Returns the quarter of the two points in a two-dimensional plane.
    :param coords: iterable, coordinates of the map cell

    :return: integer, number of the quarter
    """
    x, y = coords
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4


class Finder:
    """
    Base class.
    """

    def __init__(self, village_name):
        self.village_name = village_name

        player_villages = tkpy.Villages(DRIVER)
        player_villages.pull()
        self.coords = player_villages[self.village_name].coordinate  # coordinates of player's village

    def distance(self, cell_cords):
        """
        Calculates Euclidean distance between player's village and the cell on the map.
        :param cell_cords: coordinates of the specified map cell

        :return: integer
        """
        return math.ceil(math.sqrt((self.coords[0] - cell_cords[0]) ** 2 + (self.coords[1] - cell_cords[1]) ** 2))

    def closest(self, values):
        distances = [self.distance(v) for v in values]
        result = sorted(list(zip(distances, values)), key=lambda x: x[0])

        for d, c in result:
            print(f'Coordinates: {c}\tDistance: {d}')

# f = Finder('XDD')
# print(f.distance((13,24)))
