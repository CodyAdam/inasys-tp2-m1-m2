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