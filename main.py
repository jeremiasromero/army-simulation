from armies import (
    chinese_conf,
    english_conf,
    bizantines_conf
)

def print_army_status(army):
    print(f"\n--- {army.civilization.name} Army ---")
    print(f"Gold: {army.gold}")
    print(f"Units: {len(army.units)}")
    print(f"Total strength: {sum(unit.strength for unit in army.units)}")
    print(f"Battle history: {army.battle_history}")

def main():
    # Create armies
    chinese_army = chinese_conf.add_army()
    english_army = english_conf.add_army()

    print("Initial armies created.")
    print_army_status(chinese_army)
    print_army_status(english_army)

    # Train some units
    print("\nTraining units...")
    chinese_army.train_unit(0)   # Train first unit
    chinese_army.train_unit(1)

    # Transform a unit
    print("\nTransforming unit...")
    chinese_army.transform_unit(0)  # Pikeman -> Archer

    print_army_status(chinese_army)

    # Battle
    print("\nBattle begins!")
    winner = chinese_army.battle(english_army)

    if winner:
        print(f"\nWinner: {winner.civilization.name}")
    else:
        print("\nBattle ended in a draw")

    print_army_status(chinese_army)
    print_army_status(english_army)


if __name__ == "__main__":
    main()
