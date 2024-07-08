from enum import Enum

class myEnum(Enum):
    def toString(self) -> str:
        return self.value
    
class Type(myEnum):
    ACOUSTIC = "ecoustic"
    ELECTRIC = "electric"

class Builder(myEnum):
    FENDER = "Fender"
    MARTIN = "Martin"
    GIBSON = "Gibson"
    COLLINGS = "Collings"
    OLSON = "Olson"
    RYAN = "Ryan"
    PRS = "Prs"
    ANY = "Any"

class Wood(myEnum):
    INDIAN_ROSEWOOD = "Indian Rosewood"
    BRAZILIAN_ROSEWOOD = "Brazilian Rosewood"
    MAHOGANY = "Mahogany"
    MAPLE = "Maple"
    COCOBOLO = "Cocobolo"
    CEDAR = "Cidar"
    ADIRONDACK = "Adirondack"
    ALDER = "Alder"
    SITKA = "Sitka"
    SPRUCE = "Spruce"

class InstrumentType(myEnum):
    GUITER = "Guitar"
    BANJO = "Banjo"
    DOBRO = "Dobro"
    FIDDLE = "Fiddle"
    BASS = "Bass"
    MANDOLIN = "Mandolin"

class Style(myEnum):
    pass

class Property(myEnum):
    STYLE = "Style"
    INSTRUMENT_TYPE = "Instrument Type"
    BACK_WOOD = "Back Wood"
    TOP_WOOD = "Top Wood"
    BUILDER = "Builder"
    TYPE = "Type"
    MODEL = "Model"
    NUM_STRINGS = "Number of Strings"
