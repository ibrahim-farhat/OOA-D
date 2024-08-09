from dataclasses import dataclass, field

@dataclass()
class InstrumentSpec():
    properties: dict = field(default_factory=dict)
    
    def matches(self, other) -> bool:
        if not isinstance(other, InstrumentSpec):
            raise TypeError("Argument must be an InstrumentSpec object")
        for key, value in self.properties.items():
            if other.properties.get(key) != value:
                return False
        return True