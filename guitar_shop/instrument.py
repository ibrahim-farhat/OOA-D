from .instrumentSpec import InstrumentSpec

from dataclasses import dataclass, field

@dataclass
class Instrument():
    serialNumber: str
    price: float
    spec: InstrumentSpec

    def __post_init__(self):
        if not isinstance(self.serialNumber, str):
            ValueError("Argumet must be a str object")
        if not isinstance(self.price, float):
            raise ValueError("Argumet must be a float object")
        if not isinstance(self.spec, InstrumentSpec):
            raise ValueError("Argumet must be an InstrumentSpec object")