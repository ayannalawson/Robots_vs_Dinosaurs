import Robot
import Weapon


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()


    def create_fleet(self):
        weapon1 = Weapon("Claymore", 15)
        weapon2 = Weapon("Katana", 10)
        weapon3 = Weapon("Auto Rifle", 60)

        robot1 = Robot("Acetylene Pistol", weapon3)
        robot2 = Robot("Agonzier Blade", weapon2)
        robot3 = Robot("Anti-Gravity Gun", weapon1)

        self.robots.append(robot1)
        self.robots.append(robot2)
        self.robots.append(robot3)