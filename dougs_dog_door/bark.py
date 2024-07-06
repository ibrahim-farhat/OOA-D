from dataclasses import dataclass

@dataclass
class Bark():
    sound: str

    def getSound(self) -> str:
        return self.sound