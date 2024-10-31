Let's implement Exercise 4 (Engine004) - the Hospital Robot System using Object-Oriented Programming. Let's break it down into classes and implement them step by step.

1. First, let's create the Point class for handling robot positions:

```python:TP2/engine004/models/point.py
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
```

2. Now, let's create the base RobotC class:

```python:TP2/engine004/models/robot.py
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
```

3. Let's implement the Mobile Robot class:

```python:TP2/engine004/models/robot_mobile.py
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
```

4. Let's create specialized robot classes:

```python:TP2/engine004/models/specialized_robots.py
from .robot_mobile import RobotCMobile

class RobotSurveillance(RobotCMobile):
    def sendOrientation(self, other_robot: RobotCMobile) -> None:
        """Share orientation with another robot"""
        other_robot.setOrientation(self.orientation)

class RobotAccueil(RobotCMobile):
    def accueillir(self, visiteur: str) -> str:
        return f"Bienvenue {visiteur}!"
    
    def indiqueChemin(self, destination: str) -> str:
        return f"Pour aller à {destination}, suivez-moi."
    
    def prendreRendezVous(self, details: str) -> str:
        return f"Rendez-vous enregistré: {details}"

class RobotChirurgical(RobotC):
    def preparerInstrument(self, instrument: str) -> None:
        print(f"Préparation de {instrument}")
    
    def suivreOperation(self) -> None:
        print("Suivi de l'opération en cours")
    
    def assisterChirurgien(self) -> None:
        print("Assistance au chirurgien")

class RobotNettoyage(RobotCMobile):
    def nettoyerZone(self, zone: str) -> None:
        print(f"Nettoyage de la zone {zone}")
    
    def decontaminer(self) -> None:
        print("Décontamination en cours")
```

5. Finally, let's create a main file to demonstrate the system:

```python:TP2/engine004/main.py
from models.specialized_robots import (
    RobotSurveillance, RobotAccueil, 
    RobotChirurgical, RobotNettoyage
)

def main():
    # Create array of 4 different robots
    robots = [
        RobotSurveillance(id=1),
        RobotAccueil(id=2),
        RobotChirurgical(id=3),
        RobotNettoyage(id=4)
    ]
    
    # Demonstrate some functionalities
    surveillance_robot = robots[0]
    accueil_robot = robots[1]
    
    # Share orientation
    surveillance_robot.sendOrientation(accueil_robot)
    
    # Welcome visitor
    print(accueil_robot.accueillir("Patient"))
    
    # Clean area
    robots[3].nettoyerZone("Salle d'opération")

if __name__ == "__main__":
    main()
```

### Explanation of the Implementation:

1. **Point Class**:
   - Handles 3D coordinates
   - Implements movement with rotation and translation
   - Uses numpy for matrix operations

2. **RobotC Base Class**:
   - Private ID attribute
   - Public attributes for category, orientation, status
   - Position managed by Point class
   - Basic robot functionality

3. **RobotCMobile Class**:
   - Inherits from RobotC
   - Adds movement based on orientation
   - Uses Direction enum for clarity

4. **Specialized Robot Classes**:
   - Each implements specific functionality
   - Inherit from appropriate base class
   - Clear separation of concerns

5. **Main Program**:
   - Creates array of different robots
   - Demonstrates various robot capabilities
   - Shows interaction between robots

This implementation follows OOP principles:
- Encapsulation (private ID)
- Inheritance (specialized robots)
- Polymorphism (different robot behaviors)
- Abstraction (clear interfaces)

The system is modular and extensible, allowing for easy addition of new robot types or functionalities.


# Demo

Let's create a more comprehensive demo that showcases all robot types and their functionalities. Here's an enhanced main.py:

```python:TP2/engine004/main.py
from models.specialized_robots import (
    RobotSurveillance, RobotAccueil, 
    RobotChirurgical, RobotNettoyage
)
from models.robot import Direction

def main():
    # Create array of 4 different robots
    robots = [
        RobotSurveillance(id=1),
        RobotAccueil(id=2),
        RobotChirurgical(id=3),
        RobotNettoyage(id=4)
    ]
    
    # 1. Surveillance Robot Demo
    surveillance_robot = robots[0]
    print("\n=== Démonstration Robot de Surveillance ===")
    # Change orientation and share with reception robot
    surveillance_robot.setOrientation(Direction.EST)
    surveillance_robot.sendOrientation(robots[1])
    print(f"Robot de surveillance orienté vers: {surveillance_robot.orientation.name}")
    print(f"Robot d'accueil orienté vers: {robots[1].orientation.name}")
    
    # 2. Reception Robot Demo
    reception_robot = robots[1]
    print("\n=== Démonstration Robot d'Accueil ===")
    print(reception_robot.accueillir("Dr. Martin"))
    print(reception_robot.indiqueChemin("Bloc Opératoire"))
    print(reception_robot.prendreRendezVous("Consultation Cardiologie - 14h"))
    
    # 3. Surgical Robot Demo
    surgical_robot = robots[2]
    print("\n=== Démonstration Robot Chirurgical ===")
    surgical_robot.preparerInstrument("Scalpel")
    surgical_robot.suivreOperation()
    surgical_robot.assisterChirurgien()
    
    # 4. Cleaning Robot Demo
    cleaning_robot = robots[3]
    print("\n=== Démonstration Robot de Nettoyage ===")
    # Move to different locations and clean
    cleaning_robot.setOrientation(Direction.NORD)
    cleaning_robot.avancer(2.0)
    cleaning_robot.nettoyerZone("Couloir")
    
    cleaning_robot.setOrientation(Direction.EST)
    cleaning_robot.avancer(1.0)
    cleaning_robot.nettoyerZone("Salle d'opération")
    cleaning_robot.decontaminer()
    
    # Display final positions
    print("\n=== Positions Finales des Robots ===")
    for robot in robots:
        print(f"Robot {robot.id} ({robot.category}) - Position: "
              f"x={robot.position.x:.1f}, y={robot.position.y:.1f}, z={robot.position.z:.1f}")

if __name__ == "__main__":
    main()
```

This enhanced demo:

1. **Demonstrates all robot types**:
   - References robot.py for base functionality (lines 10-29)
   - Uses specialized_robots.py for specific behaviors (lines 4-33)
   - Utilizes robot_mobile.py for movement (lines 3-16)

2. **Shows spatial awareness**:
   - Uses Point class for positioning (lines 3-34 in point.py)
   - Demonstrates movement and orientation changes
   - Tracks positions of all robots

3. **Demonstrates inheritance hierarchy**:
   - Mobile robots use movement capabilities
   - Each robot type shows its specialized functions
   - Common attributes are accessed through base class

4. **Provides clear output sections**:
   - Separate demonstrations for each robot type
   - Shows interaction between robots
   - Displays final positions to demonstrate movement results

This demo better illustrates the OOP concepts and provides a more realistic scenario of how these robots would work together in a hospital environment.

```bash
cd TP2/engine004
python main.py
```

Output:

```bash
python .\main.py

=== Démonstration Robot de Surveillance ===
Robot de surveillance orienté vers: EST
Robot d'accueil orienté vers: EST

=== Démonstration Robot d'Accueil ===
Bienvenue Dr. Martin!
Pour aller à Bloc Opératoire, suivez-moi.
Rendez-vous enregistré: Consultation Cardiologie - 14h

=== Démonstration Robot Chirurgical ===
Préparation de Scalpel
Suivi de l'opération en cours
Assistance au chirurgien

=== Démonstration Robot de Nettoyage ===
Nettoyage de la zone Couloir
Nettoyage de la zone Salle d'opération
Décontamination en cours

=== Positions Finales des Robots ===
Robot 1 (Mobile) - Position: x=0.0, y=0.0, z=0.0
Robot 2 (Mobile) - Position: x=0.0, y=0.0, z=0.0
Robot 3 (Chirurgical) - Position: x=0.0, y=0.0, z=0.0
Robot 4 (Mobile) - Position: x=1.0, y=2.0, z=0.0
```