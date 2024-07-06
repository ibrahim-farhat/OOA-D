from .dog_door import DogDoor
from .bark import Bark
from .bark_recognizer import BarkRecognizer

from time import sleep

def dog_door_simulator():
    door: DogDoor = DogDoor()
    barkRecognizer: BarkRecognizer = BarkRecognizer(door)

    door.addAllowedBark(Bark("rowlf"))
    door.addAllowedBark(Bark("rooowlf"))
    door.addAllowedBark(Bark("rawlf"))
    door.addAllowedBark(Bark("woof"))

    print("Bruce starts barking.")
    barkRecognizer.recognize(Bark("rowlf"))
    print("\nBruce has gone outside...")
    
    sleep(10)

    print("\nBruce's all done...")
    print("...but he's stuck outside!")

    print("A small dog starts barking.")
    barkRecognizer.recognize(Bark("yip"))
    
    sleep(5)

    print("Bruce starts barking.")
    barkRecognizer.recognize(Bark("rooowlf"))
    print("\nBruce's back inside...")

