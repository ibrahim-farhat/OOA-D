from .dog_door import DogDoor

from dataclasses import dataclass

@dataclass()
class Remote():
    door: DogDoor

    def pressButton(self):
        if self.door.isOpen():
            self.door.close()
        else:
            self.door.open()

