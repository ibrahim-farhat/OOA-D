from .types import Type, Builder, Wood, InstrumentType, Property
from .instrument import Instrument
from .instrumentSpec import InstrumentSpec

from dataclasses import dataclass, field

@dataclass()
class Inventory():
    inventory: list = field(default_factory=list)

    def addInstrument(self, serialNumber: str, price: float, spec: InstrumentSpec):
        self.inventory.append(Instrument(serialNumber, price, spec))
    
    def getInstrument(self, serialNumber: str) -> Instrument:
        for instrument in self.inventory:
            if instrument.getSerialNumber() == serialNumber:
                return instrument
            
        return None
    
    def search(self, searchSpec: InstrumentSpec) -> list:
        matchingInstruments = []

        for instrument in self.inventory:
            if searchSpec.matches(instrument.getSpec()):
                matchingInstruments.append(instrument)
        
        return matchingInstruments
    
    def fillTestData(self):
        newProperties1 = dict()
        newProperties1[Property.INSTRUMENT_TYPE] = InstrumentType.GUITER
        newProperties1[Property.BUILDER] = Builder.COLLINGS
        newProperties1[Property.MODEL] = "CJ"
        newProperties1[Property.TYPE] = Type.ACOUSTIC
        newProperties1[Property.NUM_STRINGS] = 6
        newProperties1[Property.TOP_WOOD] = Wood.SPRUCE
        newProperties1[Property.BACK_WOOD] = Wood.INDIAN_ROSEWOOD
        self.addInstrument("11277", 3999.95, InstrumentSpec(newProperties1))
        newProperties2 = dict()
        newProperties2[Property.INSTRUMENT_TYPE] = InstrumentType.GUITER
        newProperties2[Property.BUILDER] = Builder.MARTIN
        newProperties2[Property.MODEL] = "D-18"
        newProperties2[Property.TYPE] = Type.ACOUSTIC
        newProperties2[Property.NUM_STRINGS] = 6
        newProperties2[Property.TOP_WOOD] = Wood.ADIRONDACK
        newProperties2[Property.BACK_WOOD] = Wood.MAHOGANY
        self.addInstrument("122784", 5495.95, InstrumentSpec(newProperties2))
        newProperties3 = dict()
        newProperties3[Property.INSTRUMENT_TYPE] = InstrumentType.GUITER
        newProperties3[Property.BUILDER] = Builder.FENDER
        newProperties3[Property.MODEL] = "stratocastor"
        newProperties3[Property.TYPE] = Type.ELECTRIC
        newProperties3[Property.NUM_STRINGS] = 6
        newProperties3[Property.TOP_WOOD] = Wood.ALDER
        newProperties3[Property.BACK_WOOD] = Wood.ALDER
        self.addInstrument("V95693", 1499.95, InstrumentSpec(newProperties3))
        newProperties4 = dict()
        newProperties4[Property.INSTRUMENT_TYPE] = InstrumentType.GUITER
        newProperties4[Property.BUILDER] = Builder.GIBSON
        newProperties4[Property.MODEL] = "SG'61 Reissue"
        newProperties4[Property.TYPE] = Type.ELECTRIC
        newProperties4[Property.NUM_STRINGS] = 6
        newProperties4[Property.TOP_WOOD] = Wood.MAHOGANY
        newProperties4[Property.BACK_WOOD] = Wood.MAHOGANY
        self.addInstrument("82765501", 1890.95, InstrumentSpec(newProperties4))
        newProperties5 = dict()
        newProperties5[Property.INSTRUMENT_TYPE] = InstrumentType.GUITER
        newProperties5[Property.BUILDER] = Builder.FENDER
        newProperties5[Property.MODEL] = "stratocastor"
        newProperties5[Property.TYPE] = Type.ELECTRIC
        newProperties5[Property.NUM_STRINGS] = 6
        newProperties5[Property.TOP_WOOD] = Wood.ALDER
        newProperties5[Property.BACK_WOOD] = Wood.ALDER
        self.addInstrument("V9512", 1549.95, InstrumentSpec(newProperties5))
        newProperties6 = dict()
        newProperties6[Property.INSTRUMENT_TYPE] = InstrumentType.GUITER
        newProperties6[Property.BUILDER] = Builder.GIBSON
        newProperties6[Property.MODEL] = "Les Paul"
        newProperties6[Property.TYPE] = Type.ELECTRIC
        newProperties6[Property.NUM_STRINGS] = 6
        newProperties6[Property.TOP_WOOD] = Wood.MAPLE
        newProperties6[Property.BACK_WOOD] = Wood.MAPLE
        self.addInstrument("70108276", 2295.95, InstrumentSpec(newProperties6))
