from dataclasses import dataclass
from collections import deque

@dataclass
class Station:
    name: str

    def __eq__(self, other):
        if isinstance(other, Station):
            return other.name.lower() == self.name.lower()
        return False
    
    def __hash__(self):
        return hash(self.name.lower())
    
@dataclass
class Connection:
    station1: Station
    station2: Station
    lineName: str

@dataclass
class Subway:
    connections: list[Connection]
    stations: list[Station]
    network: dict

    def __init__(self):
        self.connections = []
        self.stations = []
        self.network = {}

    def addStation(self, stationName: str):
        if not self.hasStation(stationName):
            newStation = Station(stationName)
            self.stations.append(newStation)

    def hasStation(self, stationName: str) -> bool:
        searchStation = Station(stationName)
        if searchStation not in self.stations:
            return False
        return True
    
    def addConnection(self, station1Name: str, station2Name: str, lineName: str):
        if self.hasStation(station1Name) and self.hasStation(station2Name):
            station1 = Station(station1Name)
            station2 = Station(station2Name)
            connection1 = Connection(station1, station2, lineName)
            self.connections.append(connection1)
            connection2 = Connection(station2, station1, lineName)
            self.connections.append(connection2)

            self.addToNetwork(station1, station2)
            self.addToNetwork(station2, station1)
        else:
            raise Exception("Invalid connection.")

    def addToNetwork(self, station1: Station, station2: Station):
        if station1 in self.network:
            if station2 not in self.network[station1]:
                self.network[station1].append(station2)
        else:
            self.network[station1] = [station2]

    def getConnection(self, station1: Station, station2: Station) -> Connection:
        for con in self.connections:
            if con.station1 == station1 and con.station2 == station2:
                return con
        return None
    
    def hasConnection(self, station1Name: str, station2Name: str, lineName: str) -> bool:
        station1 = Station(station1Name)
        station2 = Station(station2Name)

        for con in self.connections:
            if con.lineName == lineName:
                if con.station1 == station1 and con.station2 == station2:
                    return True
        
        return False
        
    def getDirections(self, startStationName: str, endStationName: str) -> list:
        if not self.hasStation(startStationName) or not self.hasStation(endStationName):
            raise Exception("Stations entered do not exist on this subway")

        start = Station(startStationName)
        end = Station(endStationName)

        if start == end:
            return []

        # Initialize data structures
        queue = deque([start])  # BFS queue
        previousStations = {start: None}  # Tracks the path

        # Perform BFS
        while queue:
            currentStation = queue.popleft()

            if currentStation == end:
                break

            for neighbor in self.network.get(currentStation, []):
                if neighbor not in previousStations:  # Visit each station only once
                    queue.append(neighbor)
                    previousStations[neighbor] = currentStation

        # Reconstruct the route
        route = []
        station = end
        while station != start:
            prevStation = previousStations.get(station)
            if prevStation is None:
                return []  # No path found
            route.insert(0, self.getConnection(prevStation, station))
            station = prevStation

        return route