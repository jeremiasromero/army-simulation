class Civilization:
    def __init__(self, name, starting_units_config):
        self.name = name
        self.starting_units_config = starting_units_config # {Pikeman: x, Archer: y, Knight: z}

    def add_army(self):
        return Army(self)

class Army: #Soldiers, Civilization, Gold, Battle History
    def __init__(self, civilization):
        self.gold = 1000
        self.civilization = civilization
        self.battle_history = []
        self.units = []
        
        #Instantiate the actual units
        for unit_class, count in civilization.starting_units_config.items():
            for _ in range(count):
                self.units.append(unit_class(age=20)) #Default age

    def train_unit(self, unit_index):
        if 0 <= unit_index < len(self.units):
            unit = self.units[unit_index]
            try: #Handles created exceptions from the transform method, such as not enough gold or invalid transformation
                cost = unit.train(self.gold)
                self.gold -= cost
                print(f"Unit trained! Strength is now {unit.strength}. Gold left: {self.gold}")
            except Exception as e:
                print(f"Training failed: {e}")
        else:
            print("Invalid unit index")

    def transform_unit(self, unit_index):
        if 0 <= unit_index < len(self.units):
            unit = self.units[unit_index]
            try: 
                #Pass armys available gold to the unit, if the army has enough, unit returns the cost and the new unit
                new_unit, cost = unit.transform(self.gold)
                self.gold -= cost
                self.units[unit_index] = new_unit #Replace the old unit
                print(f"Unit transformed! Gold left: {self.gold}")
            except Exception as e:
                print(f"Transformation failed: {e}")
        else:
            print("Invalid unit index")

    def _total_strength(self):
        total_strength = 0
        for unit in self.units:
            total_strength += unit.strength
        return total_strength


    def battle(self, other_army):
        my_strength = self._total_strength()
        enemy_strength = other_army._total_strength()

        if my_strength > enemy_strength:
            self.gold += 100
            self.battle_history.append("Win")
            other_army.battle_history.append("Loss")
            other_army._remove_best_units(2)
            print(f"{self.civilization.name} wins! Gained 100 gold. {other_army.civilization.name} lost 2 best units.")
            return self

        elif my_strength < enemy_strength:
            other_army.gold += 100
            self.battle_history.append("Loss")
            other_army.battle_history.append("Win")
            self._remove_best_units(2)
            print(f"{other_army.civilization.name} wins! Gained 100 gold. {self.civilization.name} lost 2 best units.")
            return other_army

        else:
            self.battle_history.append("Draw")
            other_army.battle_history.append("Draw")
            self._remove_weakest_unit()
            other_army._remove_weakest_unit()
            print("Draw! Both armies lost their weakest unit.")
            return None

    def _remove_best_units(self, count): #Avoids sorting/reordering self.units 
        for _ in range(count):
            if not self.units:
                break

            best_unit = max(self.units, key=lambda u: u.strength) #References the best unit
            self.units.remove(best_unit)


    def _remove_weakest_unit(self): #Avoids sorting/reordering self.units indexes
        if not self.units:
            return

        weakest_unit = min(self.units, key=lambda u: u.strength) #References the weakest unit
        self.units.remove(weakest_unit)


class Soldier:
    def __init__(self, age, strength):
        self.age = age
        self.strength = strength

    #Defines the interface in the parent class, thats why i define gold even when its not used here
    def train(self, gold):
        raise NotImplementedError("Subclasses must implement their own train method")

    def transform(self, gold):
        raise Exception("This unit cannot transform")

class Pikeman(Soldier):
    def __init__(self, age=20): #Default age for new recruits
        super().__init__(age, 5) #Strength 5

    def train(self, available_gold):
        cost = 10
        if available_gold >= cost:
            self.strength += 3
            return cost #Return the cost
        else:
            raise Exception("Not enough gold to train")

    def transform(self, available_gold):
        cost = 30
        if available_gold >= cost:
            print("Pikeman transforming into Archer...")
            return Archer(self.age), cost
        else:
            raise Exception("Not enough gold to transform")

class Archer(Soldier):
    def __init__(self, age=20): #Default age for new recruits
        super().__init__(age, 10) #Strength 10

    def train(self, available_gold):
        cost = 20
        if available_gold >= cost:
            self.strength += 7
            return cost
        else:
            raise Exception("Not enough gold to train")

    def transform(self, available_gold):
        cost = 40
        if available_gold >= cost:
            print("Archer transforming into Knight...")
            return Knight(self.age), cost
        else:
            raise Exception("Not enough gold to transform")


class Knight(Soldier):
    def __init__(self, age=20): #Default age for new recruits
        super().__init__(age, 20) #Strength 20

    def train(self, available_gold):
        cost = 30
        if available_gold >= cost:
            self.strength += 10
            return cost
        else:
            raise Exception("Not enough gold to train")

#Configs defined at the bottom, after the classes they reference are created, avoiding import errors
chinese_conf = Civilization("Chinese", {Pikeman: 2, Archer: 25, Knight: 2})
english_conf = Civilization("English", {Pikeman: 10, Archer: 10, Knight: 10})
bizantines_conf = Civilization("Bizantines", {Pikeman: 5, Archer: 8, Knight: 15})
