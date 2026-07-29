import json
import os


class Wizard:
    def __init__(self, name):
        self.name = name
        self.spells = []

    def add_spell(self, spell):
        self.spells.append(spell)

    def remove_spell(self, spell_name):
        for spell in self.spells:
            if spell["name"].lower() == spell_name.lower():
                self.spells.remove(spell)
                return True
        return False

    def display_spells(self):
        if not self.spells:
            print("No spells added yet.")
            return

        print("\nYour Spell Inventory:")
        for spell in self.spells:
            print(
                f"- {spell['name']} | "
                f"Type: {spell['type']} | "
                f"Difficulty: {spell['difficulty']}"
            )


def load_spells():
    if os.path.exists("spells.json"):
        with open("spells.json", "r") as file:
            return json.load(file)

    return []


def save_spells(spells):
    with open("spells.json", "w") as file:
        json.dump(spells, file, indent=4)


def main():

    print("🪄 Welcome to Hogwarts Spell Inventory")

    name = input("Enter wizard name: ")

    wizard = Wizard(name)
    wizard.spells = load_spells()

    while True:

        print("""
        1. View spells
        2. Add spell
        3. Remove spell
        4. Exit
        """)

        choice = input("Choose an option: ")

        if choice == "1":

            wizard.display_spells()


        elif choice == "2":

            spell_name = input("Spell name: ")
            spell_type = input("Spell type: ")
            difficulty = input("Difficulty (Easy/Medium/Hard): ")

            new_spell = {
                "name": spell_name,
                "type": spell_type,
                "difficulty": difficulty
            }

            wizard.add_spell(new_spell)

            save_spells(wizard.spells)

            print(f"{spell_name} added!")


        elif choice == "3":

            spell = input("Spell to remove: ")

            if wizard.remove_spell(spell):
                save_spells(wizard.spells)
                print("Spell removed.")
            else:
                print("Spell not found.")


        elif choice == "4":

            print("Mischief managed! 🧙")
            break


        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
