from .instrumentSpec import InstrumentSpec

from dataclasses import dataclass

@dataclass
class Instrument():
    serialNumber: str
    price: float
    spec: InstrumentSpec
    
    def getSerialNumber(self) -> str:
        return self.serialNumber
    
    def getPrice(self) -> float:
        return self.price
    
    def setPrice(self, price: float):
        self.price = price

    def getSpec(self) -> InstrumentSpec:
        return self.spec