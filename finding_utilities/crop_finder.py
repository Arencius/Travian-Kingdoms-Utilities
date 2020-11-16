import tkpy
import math
from data.user_data import DRIVER
from .finder import Finder
from requests.exceptions import HTTPError

class CropFinder(Finder):
    """
    Class for searching for crop fields. 
    """

    def __init__(self, village_name):
        super().__init__(village_name)

        game_map = tkpy.Map(DRIVER)
        game_map.pull()

        valleys = game_map.gen_abandoned_valley()
        self.valleys_filtered = list(filter(lambda x: x.coordinate.x > 0 and x.coordinate.y > 0, valleys))

    def distance(self, valley_coords):
        return super().distance(valley_coords)

    def find(self):
        """
        Searches map for abandoned valleys with 9 or 15 crop fields.

        :return: generator object with tuples of crop valleys coordinates
        """
        for v in self.valleys_filtered:
            try:
                res = v.req_details().get('resType')
                if res[-1] in ['5', '9']:
                    yield v.coordinate.x, v.coordinate.y
            except HTTPError:
                pass

    def closest_crops(self, valleys):
        super().closest(valleys)

'''
cf = CropFinder('XDD')
found_cf = cf.find()
for x in found_cf:
    print(x)
'''
#cf = CropFinder('XDD')
#found_cf = cf.find()
#for x in cf.find():
#    print(x)
#cf.closest_crops(list(found_cf))
