from .bark import Bark

from dataclasses import dataclass, field
from threading import Thread
from time import sleep

@dataclass()
class DogDoor():
    doorState: bool = field(default=False)
    allowedBarks: list = field(default_factory=list[Bark])


    def close(self):
        self.doorState = False

    def open(self):
        self.doorState = True
        Thread(target=lambda: (sleep(5), self.close())).start()

    def isOpen(self) -> bool:
        return self.doorState
    
    def addAllowedBark(self, allowedBark):
        self.allowedBarks.append(allowedBark)
    
    def getAllowedBarks(self) -> list:
        return self.allowedBarks