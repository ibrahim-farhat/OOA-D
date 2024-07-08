from .inventory import Inventory
from .types import Type, Wood, Builder, Property
from .instrument import Instrument
from .instrumentSpec import InstrumentSpec

def find_guitar_tester():
    myInventory = Inventory()
    myInventory.fillTestData()

    clientProperties = dict()
    clientProperties[Property.BUILDER] = Builder.GIBSON
    clientProperties[Property.BACK_WOOD] = Wood.MAPLE

    clientSpec = InstrumentSpec(clientProperties)
    
    foundInstruments = myInventory.search(clientSpec)    
    
    for element in foundInstruments:
        print(element)