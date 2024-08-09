from guitar_shop.find_guitar_tester import find_guitar_tester
from inspect import getmembers, isfunction
from pprint import pprint
from dougs_dog_door.bark import Bark
from guitar_shop.instrument import Instrument
from dougs_dog_door.dog_door_simulator import dog_door_simulator

# pprint(getmembers(Instrument, isfunction))
find_guitar_tester()
# dog_door_simulator()