import numpy as np

class Point:
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z
    
    def set_xyz(self, x: float, y: float, z: float) -> None:
        """Initialize robot coordinates"""
        self.x = x
        self.y = y
        self.z = z
    
    def deplace(self, dx: float, dy: float, dz: float, theta: float) -> None:
        """Move robot with rotation around Z-axis followed by translation"""
        # Rotation matrix around Z-axis
        R = np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])
        
        # Current position vector
        pos = np.array([self.x, self.y, self.z])
        
        # Translation vector
        trans = np.array([dx, dy, dz])
        
        # Apply rotation and translation
        new_pos = R @ pos + trans
        
        # Update position
        self.x, self.y, self.z = new_pos 