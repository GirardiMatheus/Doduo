import random

class Character:
    def __init__(self, name, health, level):
        self.__name = name
        self.__health = health
        self.__level = level

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_level(self):
        return self.__level

    def display_details(self):
        return f"Name: {self.get_name()}\nHealth: {self.get_health()}\nLevel: {self.get_level()}"

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0

    def attack(self, target):
        damage = random.randint(self.get_level() * 2, self.get_level() * 4)
        target.take_damage(damage)
        print(f"{self.get_name()} attacked {target.get_name()} and dealt {damage} damage!")

class Hero(Character):
    def __init__(self, name, health, level, skill):
        super().__init__(name, health, level)
        self.__skill = skill
        self.__stamina = 3  # Limit for special attacks

    def get_skill(self):
        return self.__skill

    def special_attack(self, target):
        if self.__stamina > 0:
            damage = random.randint(self.get_level() * 5, self.get_level() * 8)
            target.take_damage(damage)
            self.__stamina -= 1
            print(f"{self.get_name()} used the special skill {self.get_skill()} on {target.get_name()} and dealt {damage} damage!")
        else:
            print("Not enough stamina for a special attack!")

    def defend(self):
        print(f"{self.get_name()} is defending and takes reduced damage next turn!")

class Enemy(Character):
    def __init__(self, name, health, level, kind):
        super().__init__(name, health, level)
        self.__kind = kind

    def get_kind(self):
        return self.__kind

    def attack(self, target):
        damage = random.randint(self.get_level() * 2, self.get_level() * 3)
        target.take_damage(damage)
        print(f"{self.get_name()} ({self.get_kind()}) attacked {target.get_name()} and dealt {damage} damage!")

class Game:
    """Orchestrates the game mechanics"""
    def __init__(self):
        self.show_title()
        hero_name = input("Enter your hero's name: ")
        self.hero = Hero(name=hero_name, health=100, level=5, skill="Super Strength")
        self.enemy = self.create_random_enemy()

    def show_title(self):
        """Displays the game title"""
        print("=" * 40)
        print("        Welcome to DODUO RPG!")
        print("=" * 40)
        print("""
  ██████╗  ██████╗ ██████╗ ██╗   ██╗ ██████╗ 
  ██   ██╗██╔═══██╗██╔══██╗██║   ██║██╔═══██╗
  ██   ██║██║   ██║██   ██║██║   ██║██║   ██║
  ██   ██║██║   ██║██   ██║██║   ██║██║   ██║
  █████╔╝ ╚██████╔╝█████╔╝ ╚██████╔╝╚██████╔╝
  ╚════╝   ╚═════╝ ╚════╝   ╚═════╝  ╚═════╝ 
        """)
        print("=" * 40)

    def create_random_enemy(self):
        enemy_types = [
            {"name": "Bat", "health": 80, "level": 5, "kind": "Flying"},
            {"name": "Goblin", "health": 90, "level": 4, "kind": "Ground"},
            {"name": "Dragon", "health": 120, "level": 6, "kind": "Boss"}
        ]
        enemy_data = random.choice(enemy_types)
        return Enemy(name=enemy_data["name"], health=enemy_data["health"], level=enemy_data["level"], kind=enemy_data["kind"])

    def start_battle(self):
        """Manages the turn-based battle"""
        print("Battle Start!")
        while self.hero.get_health() > 0 and self.enemy.get_health() > 0:
            print("\n=== Current Stats ===")
            print(self.hero.display_details())
            print()
            print(self.enemy.display_details())
            print("=====================")

            input("\nPress Enter to continue...")
            choice = input("Choose (1 - Normal Attack, 2 - Special Attack, 3 - Defend): ")

            if choice == '1':
                self.hero.attack(self.enemy)
            elif choice == '2':
                self.hero.special_attack(self.enemy)
            elif choice == '3':
                self.hero.defend()
            else:
                print("Invalid choice. Try again.")

            if self.enemy.get_health() > 0:
                self.enemy.attack(self.hero)

        if self.hero.get_health() > 0:
            print("\nCongratulations! You defeated the enemy!")
        else:
            print("\nYou were defeated. Better luck next time!")

# Create and start the game
game = Game()
game.start_battle()
