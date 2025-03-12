class Hero():
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health = other.health - self.attack_power
        print(f"Игрок {self.name} атаковал {other.name} и отнял {self.attack_power} здоровья.")


    def is_alive(self):
        if self.health > 0:
            return True
        return False

class Game():
    def __init__(self, computer_health=100, computer_attack=5, player_heath=100, player_attack=20):
        self.computer = Hero("Computer", computer_health, computer_attack)
        self.player = Hero("Player", player_heath, player_attack)
    def start(self):
        n = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"Раунд {n}")
            self.computer.attack(self.player)
            if self.player.is_alive():
                self.player.attack(self.computer)

            n = n+1

game = Game()
game.start()