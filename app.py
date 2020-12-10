from finding_utilities.elephant_finder import ElephantFinder
from finding_utilities.crop_finder import CropFinder

OPTIONS = ['Elephant finder', 'Crop finder', '#TODO# Automated attacks *inactive*']


def display_options():
    print('TRAVIAN UTILITIES. CHOOSE AN OPTION:')
    for i, option in enumerate(OPTIONS):
        print(f'{i + 1}. {option}')


def mainloop():
    display_options()
    while True:
        user_input = int(input())

        if user_input == 1:
            ef = ElephantFinder('')
            found_ef = list(ef.find())
            ef.closest_elephants(found_ef)

        elif user_input == 2:
            cf = CropFinder('')
            found_c = list(cf.find())
            cf.closest_crops(found_c)


mainloop()
