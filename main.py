import random


class Player:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.a = 2  # variable for choosing options for action in action method

    # method shows information about players

    def show_information(self):
        print(f' Здоровье игрока {self.name}    {self.health}  {self.health * "+"}')

    # method shows and calculates damage.
    # variables damage_level1 and damage_level2 for start and end of damage force
    # variable type_of_damage describes type of damage force

    def damages(self, other_player, damage_level1, damage_level2, type_of_damage):
        other_player.health -= random.randint(damage_level1, damage_level2)
        print(f'{self.name} наносит {type_of_damage} урон {other_player.name}')

    # method calculates level to heal player health

    def heal_yourself(self):
        self.health += random.randint(18, 25)
        if self.health > 100:
            self.health = 100
        print(f'{self.name} исцеляет себя')

    # method chooses action type

    def action(self, other_player):
        choice = random.randint(0, self.a)
        if choice == 0:
            self.damages(other_player, 10, 35, 'сильный')
        elif choice == 1:
            self.damages(other_player, 18, 25, 'умеренный')
        else:
            self.heal_yourself()


def main(player1, player2):
    player = Player(player1)
    computer = Player(player2)

    flag = random.randint(0, 1)  # variable for choosing player
    while player.health > 0 and computer.health > 0:
        if flag:
            player.action(computer)
        else:
            if computer.health < 35:  # increase the likelihood of health recovery by the computer
                computer.a = 4
            else:
                computer.a = 2
            computer.action(player)

        player.show_information()
        computer.show_information()
        print('-' * 100)
        flag = random.randint(0, 1)

    if player.health > 0:
        print('Player is win')
    else:
        print('Computer is win')


if __name__ == '__main__':
    main('Player', 'Computer')
