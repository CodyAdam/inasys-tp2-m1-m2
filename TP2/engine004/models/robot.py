from enum import IntEnum
from .point import Point

class Direction(IntEnum):
    NORD = 1
    EST = 2
    SUD = 3
    OUEST = 4

class RobotC:
    def __init__(self, id: int, category: str):
        self.__id = id
        self.category = category
        self.orientation = Direction.NORD
        self.status = True
        self.position = Point()
    
    def getStatus(self) -> bool:
        """Get robot operational status"""
        return self.status
    
    def setOrientation(self, direction: Direction) -> None:
        """Set robot orientation"""
        self.orientation = direction
    
    @property
    def id(self) -> int:
        """Get robot ID"""
        return self.__id 