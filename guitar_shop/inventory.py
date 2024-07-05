from .guitar import Guitar, GuitarSpec
from .types import Type, Builder, Wood
from dataclasses import dataclass, field

@dataclass()
class Inventory():
    guitars: list = field(default_factory=list)

    def fillJunkData(self):
        self.guitars.append(Guitar("Inv-000", 1249.99, GuitarSpec(Builder.FENDER, "Stratocastor", Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 12)))
        self.guitars.append(Guitar("Inv-111", 799.99, GuitarSpec(Builder.ANY, "Stratocastor", Type.ACOUSTIC, Wood.ADIRONDACK, Wood.ADIRONDACK, 10)))
        self.guitars.append(Guitar("Inv-122", 549.99, GuitarSpec(Builder.ANY, "Stratocastor", Type.ACOUSTIC, Wood.ADIRONDACK, Wood.ADIRONDACK, 10)))
        self.guitars.append(Guitar("Inv-133", 799.99, GuitarSpec(Builder.ANY, "Stratocastor", Type.ACOUSTIC, Wood.ADIRONDACK, Wood.ADIRONDACK, 1)))
        self.guitars.append(Guitar("Inv-222", 899.99, GuitarSpec(Builder.GIBSON, "Stratocastor", Type.ELECTRIC, Wood.BRAZILIAN_ROSEWOOD, Wood.BRAZILIAN_ROSEWOOD, 3)))
        self.guitars.append(Guitar("Inv-333", 949.99, GuitarSpec(Builder.COLLINGS, "Stratocastor", Type.ACOUSTIC, Wood.COCOBOLO, Wood.COCOBOLO, 4)))
        self.guitars.append(Guitar("Inv-444", 349.99, GuitarSpec(Builder.MARTIN, "Stratocastor", Type.ELECTRIC, Wood.CEDAR, Wood.CEDAR, 6)))
        self.guitars.append(Guitar("Inv-555", 239.99, GuitarSpec(Builder.OLSON, "Stratocastor", Type.ACOUSTIC, Wood.INDIAN_ROSEWOOD, Wood.INDIAN_ROSEWOOD, 17)))
        self.guitars.append(Guitar("Inv-666", 1599.99, GuitarSpec(Builder.PRS, "Stratocastor", Type.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY, 5)))
        self.guitars.append(Guitar("Inv-777", 3999.99, GuitarSpec(Builder.RYAN, "Stratocastor", Type.ACOUSTIC, Wood.MAPLE, Wood.MAPLE, 8)))
        self.guitars.append(Guitar("Inv-888", 569.99, GuitarSpec(Builder.FENDER, "Stratocastor", Type.ACOUSTIC, Wood.SITKA, Wood.SITKA, 5)))
        self.guitars.append(Guitar("Inv-999", 1099.99, GuitarSpec(Builder.GIBSON, "Stratocastor", Type.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD, Wood.INDIAN_ROSEWOOD, 7)))        

    def addGuitar(self, serialNumber: str,
                  price: float,
                  spec: GuitarSpec):
        
        self.guitars.append(Guitar(serialNumber,
                                          price,
                                          spec))
    
    def getGuitar(self, serialNumber: str) -> Guitar:
        for element in self.guitars:
            if element.getSerialNumber() == serialNumber:
                return element
        return None
    
    def search(self, searchSpec: GuitarSpec):
        matchingGuitars = []

        for element in self.guitars:
            if searchSpec == element.getSpec():
                matchingGuitars.append(element)
        
        return matchingGuitars