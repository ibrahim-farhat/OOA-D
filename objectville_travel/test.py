import sys
from pathlib import Path

from .loader import SubwayLoader
from .subway import Subway
from .printer import SubwayPrinter

def objectvilleSubwayTester():
    try:
        loader = SubwayLoader()
        objectville = loader.loadFromFile("objectville_travel/ObjectvilleSubway.txt")

        print("Testing stations")
        if objectville.hasStation("DRY Drive") and \
           objectville.hasStation("Weather-O-Rama, Inc.") and \
           objectville.hasStation("Boards 'R' Us"):
            print("... station test passed successfully.")
        else:
            print("...station test FAILED.")
            exit(-1)

        print("\nTesting connections...")
        if objectville.hasConnection("DRY Drive", "Head First Theater", "Meyer Line") and \
           objectville.hasConnection("LSP Lane", "JavaBeans Boulevard", "Booch Line") and \
           objectville.hasConnection("OOA&D Oval", "Head First Labs", "Gamma Line"):
            print("...connections test passed succesfully.")
        else:
            print("...connections test FAILED")
            # exit(-1)

    except Exception as e:
        print(e)

def getDirectionsTester(args):
    if len(args) != 2:
        print("Usage: SubwayTester [StartStation] [endStation]", file=sys.stderr)
        sys.exit(-1)
    try:
        loader = SubwayLoader()
        objectville = loader.loadFromFile(Path("objectville_travel/ObjectvilleSubway.txt"))

        if not objectville.hasStation(args[0]):
            print(f"{args[0]} is not a station in Objectville", file=sys.stderr)
            sys.exit(-1)
        elif not objectville.hasStation(args[1]):
            print(f"{args[1]} is not a station in Objectville", file=sys.stderr)
            sys.exit(-1)
        route = objectville.getDirections(args[0], args[1])
        printer = SubwayPrinter(sys.stdout)
        printer.printDirections(route)

    except Exception as e:
        print(e, file=sys.stdout)
