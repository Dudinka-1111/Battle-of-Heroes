class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name}, отнимая здоровье в размере {self.attack_power}.")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Game:
    def __init__(self, player_name='Воин', computer_name='Компьютер'):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра начинается!")
        print(f"Здоровье игроков в начале игры: {self.computer.name} = {self.computer.health}, {self.player.name} = {self.player.health} ")

        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if not self.computer.is_alive():
                break
            self.computer_turn()

        self.declare_winner()

    def player_turn(self):
        self.player.attack(self.computer)
        print(f"У {self.computer.name} осталось {self.computer.health} здоровья.\n")

    def computer_turn(self):
        self.computer.attack(self.player)
        print(f"У {self.player.name} осталось {self.player.health} здоровья.\n")

    def declare_winner(self):
        if self.player.is_alive():
            print(f"{self.player.name} побеждает!")
        else:
            print(f"{self.computer.name} побеждает!")


if __name__ == "__main__":
    game = Game('Воин')
    game.start()