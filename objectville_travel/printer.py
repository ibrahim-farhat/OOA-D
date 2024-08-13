import sys

class SubwayPrinter:
    def __init__(self, out=sys.stdout):
        self.out = out

    def printDirections(self, route):
        if len(route) == 0:
            print("No way to go to your station.")
            return
        
        connection = route[0]
        currentLine = connection.lineName
        previousLine = currentLine
        

        print(f"Start out at {connection.station1.name}.", file=self.out)
        print(f"Get on the {currentLine} heading towards {connection.station2.name}.", file=self.out)
        
        for i in range(1, len(route)):
            connection = route[i]
            currentLine = connection.lineName
            if currentLine == previousLine:
                print(f"  Continue past {connection.station1.name}...", file=self.out)
            else:
                print(f"When you get to {connection.station1.name}, get off the {previousLine}.", file=self.out)
                print(f"Switch over to the {currentLine}, heading towards {connection.station2.name}.", file=self.out)
                previousLine = currentLine
        
        print(f"Get off at {connection.station2.name} and enjoy yourself!", file=self.out)
