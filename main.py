import random

TOWNHALL_LEVEL = 1
GOLD = 1000
ELIXIR = 1000
TROOP_CAPACITY = 20

class Player:
    def __init__(self, name):
        self.name = name
        self.townhall_level = TOWNHALL_LEVEL
        self.gold = GOLD
        self.elixir = ELIXIR
        self.troop_capacity = TROOP_CAPACITY
        self.troops = []

    def print_resources(self):
        print(f"Gold: {self.gold}")
        print(f"Elixir: {self.elixir}")

    def print_troops(self):
        print("Troops: ")
        for troop in self.troops:
            print(troop)

    def attack(self):
        enemy_townhall_level = random.randint(1,10)
        if self.townhall_level > enemy_townhall_level:
            print("You won the attack!")
        else:
            print("You lost the attack!")

    def train_troop(self, troop):
        if len(self.troops) >= self.troop_capacity:
            print("Troop capacity reached, Upgrade your camps to train more troops")
        else:
            if self.gold >= troop.cost:
                self.gold -= troop.cost
                self.troops.append(troop)
            else:
                print("Not enough god to train the toops")


class Troops:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        return f"{self.name} - Cost: {self.cost}"

def game_loop():
    print("Welcome to Clash of Clans (CLI Version)!")
    player_name = input("Enter Your Name: ")
    player = Player(player_name)

    while True:
        print("\n[MAIN MENU]")
        print("1. Print Resouces")
        print("2. Print Troops")
        print("3. Train Troops")
        print("4. Attack ")
        print("5. Quit ")
        choice = input("Enter your choices: ")

        if choice == "1":
            player.print_resources()
        elif choice == "2":
            player.print_troops()
        elif choice == "3":
            troop_name = input("Enter the Troop name: ")
            troop_cost = int(input("Enter the troop cost: "))
            troop = Troops(troop_name, troop_cost)
            player.train_troop(troop)
        elif choice == "4":
            player.attack()
        elif choice == "5":
            print("Thanks for Playing Clash of Clans (CLI version)!")
            break
        else:
            print("Invalid choice .please try again.")


game_loop()

