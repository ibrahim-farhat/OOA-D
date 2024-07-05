from .guitar import GuitarSpec
from .inventory import Inventory
from .types import Type, Wood, Builder

def find_guitar_tester():
    myInventory = Inventory()
    myInventory.fillJunkData()

    whatErinLikes = GuitarSpec(Builder.ANY, "Stratocastor", Type.ACOUSTIC, Wood.ADIRONDACK, Wood.ADIRONDACK, 10)
    
    foundGuitars = myInventory.search(whatErinLikes)    

    for element in foundGuitars:
        print(f"We have a {element.getSpec().getBuilder().toString()} {element.getSpec().getModel()} {element.getSpec().getType().toString()} guitar:\
              \n{element.getSpec().getBackWood().toString()} back and sides,\
              \n{element.getSpec().getTopWood().toString()} top.\
              \nYou can have it for only ${element.getPrice()}!\n --------------")
