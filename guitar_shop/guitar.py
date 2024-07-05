from .types import Type, Builder, Wood
from dataclasses import dataclass

@dataclass()
class GuitarSpec():
    builder: Builder
    model: str
    type: Type
    backWood: Wood
    topWood: Wood
    numStrings: int

    def getBuilder(self) -> Builder:
        return self.builder

    def getModel(self) -> str:
        return self.model
    
    def getType(self) -> Type:
        return self.type

    def getBackWood(self) -> Wood:
        return self.backWood
    
    def getTopWood(self) -> Wood:
        return self.topWood

    def getNumStrings(self) -> int:
        return self.numStrings
    
    def __eq__(self, other):
        if isinstance(other, GuitarSpec):
            return (self.builder == other.builder and
                    self.model.lower() == other.model.lower() and
                    self.type == other.type and
                    self.backWood == other.backWood and
                    self.topWood == other.topWood and
                    self.numStrings == other.numStrings)
        
        return False

@dataclass()
class Guitar():
    serialNumber: str
    price: float
    spec: GuitarSpec

    def getSerialNumber(self) -> str:
        return self.serialNumber
    
    def getPrice(self) -> float:
        return self.price
    
    def setPrice(self, price: float) -> None:
        self.price = price

    def getSpec(self):
        return self.spec