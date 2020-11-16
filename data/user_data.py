"""
Module contains constant values about user. 
Please fill the empty places with your account data.
"""

import tkpy

USER_MAIL = ''
USER_PASSWORD = ''
GAME_WORLD = ''

DRIVER = tkpy.authenticate(email = USER_MAIL, 
                        password = USER_PASSWORD, gameworld_name = GAME_WORLD)