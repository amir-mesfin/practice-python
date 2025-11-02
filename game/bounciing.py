import random
import time
import os

class TextAdventure:
    def __init__(self):
        self.player_health = 100
        self.player_gold = 0
        self.inventory = []
        self.location = "forest"
        self.game_over = False

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self):
        print("=" * 50)
        print("          TEXT ADVENTURE GAME")
        print("=" * 50)
        print(f"Health: {self.player_health} | Gold: {self.player_gold}")
        print(f"Location: {self.location.capitalize()}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")
        print("-" * 50)

    def forest(self):
        self.clear_screen()
        self.print_header()
        print("You are in a dark forest. Tall trees surround you.")
        print("Paths lead in different directions.")
        print("\nWhat do you want to do?")
        print("1. Go to the cave")
        print("2. Go to the river")
        print("3. Search for items")
        print("4. Check inventory")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            self.cave()
        elif choice == "2":
            self.river()
        elif choice == "3":
            self.search_forest()
        elif choice == "4":
            self.show_inventory()
        else:
            print("Invalid choice!")
            time.sleep(1)
            self.forest()

    def cave(self):
        self.clear_screen()
        self.print_header()
        print("You enter a dark cave. It's cold and damp.")

        if "torch" not in self.inventory:
            print("It's too dark to see anything!")
            print("You need a torch to explore further.")
            input("\nPress Enter to return to forest...")
            self.forest()
            return

        print("With your torch, you can see glittering objects.")
        print("\nWhat do you want to do?")
        print("1. Search for treasure")
        print("2. Go deeper")
        print("3. Return to forest")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            self.find_treasure()
        elif choice == "2":
            self.fight_monster()
        elif choice == "3":
            self.forest()
        else:
            print("Invalid choice!")
            time.sleep(1)
            self.cave()

    def river(self):
        self.clear_screen()
        self.print_header()
        print("You arrive at a peaceful river.")
        print("The water looks clean and refreshing.")
        print("\nWhat do you want to do?")
        print("1. Drink water (+10 health)")
        print("2. Fish for food")
        print("3. Follow the river")
        print("4. Return to forest")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            self.player_health = min(100, self.player_health + 10)
            print("You drink the clean water and feel refreshed! +10 Health")
            time.sleep(2)
            self.river()
        elif choice == "2":
            self.fish()
        elif choice == "3":
            self.follow_river()
        elif choice == "4":
            self.forest()
        else:
            print("Invalid choice!")
            time.sleep(1)
            self.river()

    def search_forest(self):
        self.clear_screen()
        self.print_header()
        print("You search the forest...")
        time.sleep(2)

        found_items = [
            ("a shiny gold coin", "gold", 5),
            ("a healing herb", "herb", 0),
            ("an old torch", "torch", 0),
            ("a sharp stone", "stone", 0),
            ("nothing useful", None, 0)
        ]

        item, action, value = random.choice(found_items)
        print(f"You found {item}!")

        if action == "gold":
            self.player_gold += value
            print(f"+{value} gold!")
        elif action == "herb":
            self.player_health = min(100, self.player_health + 20)
            print("You use the herb and feel better! +20 Health")
        elif action and action not in self.inventory:
            self.inventory.append(action)
            print(f"Added {action} to inventory!")

        input("\nPress Enter to continue...")
        self.forest()

    def find_treasure(self):
        self.clear_screen()
        self.print_header()
        print("You search the cave and find a treasure chest!")
        treasure = random.randint(20, 50)
        self.player_gold += treasure
        print(f"You found {treasure} gold coins!")

        if random.random() > 0.7:
            special_item = random.choice(["diamond", "ancient sword", "magic amulet"])
            self.inventory.append(special_item)
            print(f"You also found a {special_item}!")

        input("\nPress Enter to continue...")
        self.cave()

    def fight_monster(self):
        self.clear_screen()
        self.print_header()
        print("A giant spider attacks you!")
        time.sleep(2)

        monster_health = 30
        print(f"Monster Health: {monster_health}")

        while monster_health > 0 and self.player_health > 0:
            print("\n1. Attack with weapon")
            print("2. Use item")
            print("3. Try to run")

            choice = input("\nWhat do you do? ")

            if choice == "1":
                damage = random.randint(5, 15)
                monster_health -= damage
                print(f"You hit the monster for {damage} damage!")

                if monster_health <= 0:
                    print("You defeated the monster!")
                    reward = random.randint(10, 25)
                    self.player_gold += reward
                    print(f"You found {reward} gold on the monster!")
                    break

                # Monster attacks back
                monster_damage = random.randint(5, 12)
                self.player_health -= monster_damage
                print(f"The monster attacks you for {monster_damage} damage!")

            elif choice == "2":
                if "herb" in self.inventory:
                    self.inventory.remove("herb")
                    heal = random.randint(15, 25)
                    self.player_health = min(100, self.player_health + heal)
                    print(f"You used a herb and healed {heal} health!")
                else:
                    print("You don't have any healing items!")
                continue
            elif choice == "3":
                if random.random() > 0.5:
                    print("You escaped successfully!")
                    break
                else:
                    print("You failed to escape!")
                    monster_damage = random.randint(8, 15)
                    self.player_health -= monster_damage
                    print(f"The monster attacks you for {monster_damage} damage!")
            else:
                print("Invalid choice!")
                continue

            print(f"\nYour health: {self.player_health}")
            print(f"Monster health: {monster_health}")
            time.sleep(1)

        if self.player_health <= 0:
            self.game_over = True
            return

        input("\nPress Enter to continue...")
        self.cave()

    def fish(self):
        self.clear_screen()
        self.print_header()
        print("You try to catch some fish...")
        time.sleep(2)

        if random.random() > 0.3:
            print("You caught a fish!")
            heal = random.randint(5, 15)
            self.player_health = min(100, self.player_health + heal)
            print(f"You eat the fish and restore {heal} health!")
        else:
            print("You didn't catch anything.")

        input("\nPress Enter to continue...")
        self.river()

    def follow_river(self):
        self.clear_screen()
        self.print_header()
        print("You follow the river and discover a hidden village!")
        print("The villagers are friendly and offer you help.")

        if self.player_health < 80:
            heal_amount = 100 - self.player_health
            self.player_health = 100
            print(f"The villagers heal you completely! +{heal_amount} health")

        if self.player_gold < 30:
            gift = random.randint(10, 20)
            self.player_gold += gift
            print(f"The villagers give you {gift} gold as a gift!")

        input("\nPress Enter to return to river...")
        self.river()

    def show_inventory(self):
        self.clear_screen()
        self.print_header()
        print("Your Inventory:")
        if not self.inventory:
            print("Empty")
        else:
            for item in self.inventory:
                print(f"- {item}")
        input("\nPress Enter to continue...")
        self.forest()

    def start_game(self):
        print("Welcome to the Text Adventure Game!")
        print("Explore the world, find treasure, and survive!")
        input("\nPress Enter to begin your adventure...")

        while not self.game_over:
            if self.location == "forest":
                self.forest()

            if self.player_health <= 0:
                self.clear_screen()
                print("GAME OVER")
                print("You have been defeated!")
                print(f"Final Score: {self.player_gold} gold")
                break

# Start the game
if __name__ == "__main__":
    game = TextAdventure()
    game.start_game()
