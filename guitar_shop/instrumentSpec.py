from dataclasses import dataclass, field

@dataclass()
class InstrumentSpec():
    properties: dict = field(default_factory=dict)

    def getProperty(self, property: str) -> object:
        return self.properties.get(property)

    def getProperties(self) -> dict:
        return self.properties.copy()
    
    def matches(self, other) -> bool:
        if not isinstance(other, InstrumentSpec):
            raise TypeError("Argument must be an InstrumentSpec object")
        for key, value in self.getProperties().items():
            if other.getProperty(key) != value:
                return False
        return True