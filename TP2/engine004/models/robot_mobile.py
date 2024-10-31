from .robot import RobotC, Direction

class RobotCMobile(RobotC):
    def __init__(self, id: int):
        super().__init__(id, "Mobile")
    
    def avancer(self, distance: float = 1.0) -> None:
        """Move robot based on orientation"""
        if self.orientation == Direction.EST:
            self.position.x += distance
        elif self.orientation == Direction.OUEST:
            self.position.x -= distance
        elif self.orientation == Direction.NORD:
            self.position.y += distance
        elif self.orientation == Direction.SUD:
            self.position.y -= distance 