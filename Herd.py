import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()


    def create_herd(self):
        dino1 = Dinosaur("Velocirator", 10)
        dino2 = Dinosaur("Pterodactyl", 15)
        dino3 = Dinosaur("Giganotosaurus", 60)

        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)