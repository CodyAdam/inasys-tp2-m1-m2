from .robot import RobotC
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
    def __init__(self, id: int):
        super().__init__(id, "Chirurgical")
    
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