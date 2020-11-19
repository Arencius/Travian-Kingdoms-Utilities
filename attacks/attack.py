""" Module containing the Attack class used create automaded attack list. """
import tkpy
from data.user_data import DRIVER

MY_VILLAGE_NAME = '' # temporary constant until I haven't added the possibility to change villages

def attacking_village():
    """ Returns the village from which the attack is sent. """
    villages = tkpy.Villages(DRIVER)
    villages.pull()

    return villages[MY_VILLAGE_NAME]

class Attack:
    def __init__(self, troops, time, coordinates, every=24):
        """
        :param troops: dictionary of troops sent for the Attack
        :param time: time of the first attack 
        :param coords: coordinates of the attacked village
        :param every: every how many hours attack will be sent. Default 24 - only once per day. """

        self.troops = troops 
        self.time = time 
        self.coordinates = coordinates
        self.every = every

        self.village = attacking_village()

    def send_attack(self):
        """ Sends the attack."""
        x,y = self.coordinates
        try:
            self.village.send_attack(x = x,y = y,units = self.troops)
        except SyntaxError:
            pass