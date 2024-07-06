from .dog_door import DogDoor
from .bark import Bark

from dataclasses import dataclass

@dataclass()
class BarkRecognizer():
    door: DogDoor

    def recognize(self, bark: Bark):
        allowedBarks = self.door.getAllowedBarks()
        recognizedFlag = False

        for allowedBark in allowedBarks:
            if allowedBark == bark:
                recognizedFlag = True
                break

        if recognizedFlag == True:
            self.door.open()