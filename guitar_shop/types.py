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