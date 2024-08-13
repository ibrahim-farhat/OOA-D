from dataclasses import dataclass
import csv

from .subway import Subway

@dataclass
class SubwayLoader:
    subway: Subway

    def __init__(self):
        self.subway = Subway()

    def loadFromFile(self, filePath):
        with open(filePath, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            self.loadStations(reader)
            
            while True:
                try:
                    lineName  = next(reader)[0]
                    self.loadLine(self.subway, reader, lineName)
                except StopIteration:
                    break

        return self.subway
    
    def loadStations(self, reader):
        for stationName in reader:
            if stationName and stationName[0]:
                self.subway.addStation(stationName[0])
            else:
                break
    
    def loadLine(self, subway, reader, lineName):
        i = 0
        station1Name = str
        station2Name = str
        for row in reader:
            if not row:
                break

            if i == 0:
                station1Name = row[0]
            else:
                if i > 1:
                    station1Name = station2Name
                station2Name = row[0]
                subway.addConnection(station1Name, station2Name, lineName)
            
            i += 1