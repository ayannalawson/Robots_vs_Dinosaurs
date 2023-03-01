import Robot
import Dinosaur
import Herd
import Fleet
import random

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.team =  self.choose_team()
        self.battle()

    def display_welcome(self):
        print(f'Welcome to Roooobots vs Dinosaursss!!!')




        print('Each Robot and Dinosaur starts the match with 200 health.')
        print('Every character begins with 150 power points.')
        print('One Attack costs 20 power points.')
        print('With the Fleet of Robots and the Herd of Dinosaurs.. Only one squad remains!!')

    def choose_team(self):
        choose_team = int(input('Choose your team: (1) Robots; (2) Dinosaurs'))
        if choose_team == 1:
            print('You chose the fleet of Robots')
            return choose_team
        elif choose_team == 2:
            print('You chose the herd of Dinosaurs')
            return choose_team
        else:
            print('Invalid answer. Try again.')
            self.choose_team()



    def battle(self):
        first_turn = random.randint(1,2)
        if first_turn == 1:
            print('Ready...FIGHT!!')
            first_turn = 1
        if first_turn == 2:
            print('Ready...FIGHT!!')
            first_turn = 2


        if first_turn == 1:
            while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
                if self.fleet.robots[0].health > 0 or self.herd.dinosaurs[0].health > 0:

                    self.robot_turn()  # First turn team


                    if self.herd.dinosaurs[0].health <= 0:
                        print(f'{self.herd.dinosaurs[0].type} is out.') 
                        self.herd.dinosaur.remove(self.herd.dinosaur[0])
                    elif self.fleet.robots[0].health <= 0:
                        print(f'{self.fleet.robots[0].name} is out')
                        self.fleet.robots.remove(self.fleet.robots[0])

                    if len(self.fleet.robots) == 0:
                        self.display_winners_dinosaurs()
                        return
                    elif len(self.herd.dinosaurs) ==0:
                        self.display_winners_robots()
                        return
                    
                    self.dino_turn()    #Second turn team

                    if self.herd.dinosaurs[0].health <= 0:
                        print(f'{self.herd.dionsaurs[0].type} is out.')
                        self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
                    elif self.fleet.robots[0].health <= 0:
                        print(f'{self.fleet.robots[0].name} is out.')
                        self.fleet.robots.remove(self.fleet.robots[0])

                    if len(self.fleet.robots) == 0:
                        self.display_winner_dinosaurs()
                        return
                    elif len(self.herd.dinosaurs) == 0:
                        self.display_winners_robots()
                        return
        elif first_turn == 2:
            while len(self.fleet.robots) > 0 and len(self.herd.dinosaurs) > 0:
                if self.fleet.robots[0].health > 0 or self.herd.dinosaurs[0].health > 0:

                    self.dino_turn()  #First turn team

                    if self.herd.dinosaurs[0].health <= 0:
                        print(f'{self.herd.dinosaurs[0].type} is out.')
                        self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
                    elif self.fleet.robots[0].health <= 0:
                        print(f'{self.fleet.robots[0].name} is out.')
                        self.fleet.robots.remove(self.fleet.robots[0])

                    if len(self.fleet.robots) ==0:
                        self.display_winners_dinosaurs()
                        return
                    elif len(self.herd.dinosaurs) ==0:
                        self.display_winners_robots()
                        return
                    

                    self.robo_turn()  #Second turn team

                    if self.herd.dinosaurs[0].health <= 0:
                        print(f'{self.herd.dinosaurs[0].type} is out.')
                        self.herd.dinosaurs.remove(self.herd.dinosaurs[0])
                    elif self.fleet.robots[0].health <=0:
                        print(f'{self.fleet.robots[0].name} is out.')
                        self.fleet.robots.remove(self.fleet.robots[0])

                    if len(self.fleet.robots) == 0:
                        self.display_winners_dinosaurs()
                        return
                    elif len(self.herd.dinosaurs) == 0:
                        self.display_winners_robots()
                        return
        def dino_turn(self):
            self.show_dino_opponent_options()
            self.herd.dinosaurs[0].attack_robot(self.fleet.robots[0])

        def robo_turn(self):
             self.show_robo_opponent_options()
             self.fleet.robots[0].attack_dinosaur(self.herd.dinosaurs[0])


    #   def dino_turn_test(self):
    #     # if  #all three on both teams still alive... etc for all combos
    #
    #     dino_selection = input(
    #         f'Choose your dinosaur: 1: {self.herd.dinosaurs[0].type}, 2: {self.herd.dinosaurs[1].type}, or 3: {self.herd.dinosaurs[2].type}')
    #     robot_attack_selection = input(
    #         f'Choose your robot to attack: 1: {self.fleet.robots[0].name}, 2: {self.fleet.robots[1].name}, or 3: {self.fleet.robots[2].name}')
    #     if dino_selection == 1 and robot_attack_selection == 1:
    #         self.herd.dinosaurs[0].attack_robot(self.fleet.robots[0])

      def show_dino_opponent_options(self):
        i = 1
        for element in self.fleet.robots:
            print(f'{element.name} has {element.health} health.')
            i += 1


    def show_robo_opponent_options(self):
        i = 1
        for element in self.herd.dinosaurs:
            print(f'{element.type} has {element.health} health.')
            i += 1


    def display_winners_robots(self):
        # print('Beep Boop! The Robot fleet has defeated the herd of Dinosaurs win.')

        if self.team == 1:
            print("The Robot fleet has defeated the herd of Dinosaurs win. You win!")
        if self.team == 2:
            print("The Robot fleet has defeated the herd of Dinosaurs win. You lose.")
        # print('Test - Robots win. Display winner message not working')


    def display_winners_dinosaurs(self):
        # print('Rawr! The herd of Dinosaurs has defeated the fleet of Robots.')

        if self.team == 2:
            print("The herd of Dinosaurs has defeated the fleet of Robots. You win!")
        if self.team == 1:
            print("The herd of Dinosaurs has defeated the fleet of Robots. You lose.")



  
  
  
  
  
  
  
  
    def battle_phase(self):
        while self.robot.health >= 0 and self.dinosaur.health >= 0 :
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
    
    def display_winner(self):
        if self.robot.health == 0 :
            print(f'{self.dinosaur.name} CONGRATULATIONS! YOU ARE THE WINNER!!!')
        else:
            print(f'{self.robot.name} CONGRATULATIONS! YOU ARE THE WINNER!!!')
        pass
