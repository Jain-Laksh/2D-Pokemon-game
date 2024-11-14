import random

class Move:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __repr__(self):
        return f"{self.name} (Damage: {self.damage})"

# Define all the moves
ember = Move("Ember", 25)
scratch = Move("Scratch", 10)
tackle = Move("Tackle", 10)
vine_whip = Move("Vine Whip", 25)
water_gun = Move("Water Gun", 25)
peck = Move("Peck", 15)
smokescreen = Move("Smokescreen", 0)  
quick_attack = Move("Quick Attack", 20)
bite = Move("Bite", 20)
solar_beam = Move("Solar Beam", 40)
earthquake = Move("Earthquake", 50)
flamethrower = Move("Flamethrower", 45)
hydro_pump = Move("Hydro Pump", 40)

class Pokemon:
    def __init__(self, name, level, experience, health, moves, pokemon_type):
        self.name = name
        self.level = level
        self.experience = experience
        self.health = health
        self.max_health = health
        self.pokemon_type = pokemon_type 
        self.moves = moves  # List of Move objects

    def level_up(self):
        """Increase level and health as the Pokémon levels up."""
        print(f"{self.name} has leveled up from {self.level} to {self.level + 1}")
        print(f"HP +15")
        self.level += 1
        self.health += 15
        self.max_health += 15
        self.experience = 0
        if self.level in [6,8,11]:
            self.moves = self.moves + [self.move_pool()]
            print(f"Your pokemon has learnt {str(self.move_pool())}")

    def take_damage(self, damage, attacker_type):
        """Reduce health based on damage, considering type effectiveness."""
        effectiveness = self.get_type_effectiveness(attacker_type)
        total_damage = damage +  effectiveness*10
        self.health -= total_damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {total_damage:.2f} damage from {attacker_type} type attack.")

    def attack(self, other, move):
        """Attack another Pokémon with a chosen move, considering type advantage."""
        print(f"{self.name} uses {move.name}!")
        other.take_damage(move.damage, self.pokemon_type)

    def get_type_effectiveness(self, attacker_type):
        """Determine the type effectiveness based on the attacker's type."""
        # Define a simple type effectiveness dictionary
        effectiveness = {
            "Fire": {"Grass": 1.0, "Water": -0.5, "Fire": 0},  # Fire is strong against Grass, weak against Water
            "Water": {"Fire": 1.0, "Grass": -0.5, "Water": 0},  # Water is strong against Fire, weak against Grass
            "Grass": {"Water": 1.0, "Fire": -0.5, "Grass": 0},  # Grass is strong against Water, weak against Fire
        }
        
        # Get effectiveness multiplier (default 1.0 for no advantage)
        return effectiveness.get(attacker_type, {}).get(self.pokemon_type, 0)

    def move_pool(self):
        """Determine the new moves learnt based on the attacker's level."""
        move_pool = {
            "Fire": {8: ember,6:quick_attack,   11: flamethrower },
            "Water": {8: water_gun, 6: peck, 11: hydro_pump}, 
            "Grass": {8: vine_whip, 6: quick_attack, 11: solar_beam}
        }
        
        return move_pool.get(self.pokemon_type, {}).get(self.level, tackle)

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        moves_str = "\n".join(str(move) for move in self.moves)
        return f"{self.name} (Level: {self.level}, Health: {self.health}/{self.level * 10}, Type: {self.pokemon_type})\nMoves:\n{moves_str}"


## Possible pokemon encounters in grass
possible_pokemon = [
    {"name": "Charmander", "level": 5, "health": 50, "moves": [ember, scratch], "type": "Fire"},
    {"name": "Squirtle", "level": 4, "health": 40, "moves": [water_gun, tackle], "type": "Water"},
    {"name": "Bulbasaur", "level": 6, "health": 50, "moves": [tackle, vine_whip], "type": "Grass"},
    {"name": "Cyndaquil", "level": 5, "health": 45, "moves": [ember, tackle], "type": "Fire"},
    {"name": "Totodile", "level": 5, "health": 45, "moves": [water_gun, scratch], "type": "Water"},
    {"name": "Chikorita", "level": 4, "health": 40, "moves": [tackle, vine_whip], "type": "Grass"},
    {"name": "Torchic", "level": 7, "health": 55, "moves": [ember, peck], "type": "Fire"},
    {"name": "Mudkip", "level": 6, "health": 50, "moves": [water_gun, tackle], "type": "Water"},
    {"name": "Treecko", "level": 5, "health": 45, "moves": [quick_attack, vine_whip], "type": "Grass"},
    {"name": "Vulpix", "level": 5, "health": 40, "moves": [ember, quick_attack], "type": "Fire"},
    {"name": "Piplup", "level": 6, "health": 50, "moves": [water_gun, peck], "type": "Water"},
    {"name": "Magmar", "level": 6, "health": 45, "moves": [ember, smokescreen], "type": "Fire"},
    {"name": "Simisage", "level": 6, "health": 50, "moves": [vine_whip, bite], "type": "Grass"},
    {"name": "Charmander", "level": 4, "health": 40, "moves": [ember, scratch], "type": "Fire"},
    {"name": "Squirtle", "level": 5, "health": 45, "moves": [water_gun, tackle], "type": "Water"},
    {"name": "Bulbasaur", "level": 4, "health": 40, "moves": [tackle, vine_whip], "type": "Grass"},
    {"name": "Chikorita", "level": 3, "health": 35, "moves": [tackle, vine_whip], "type": "Grass"},
    {"name": "Torchic", "level": 6, "health": 50, "moves": [ember, peck], "type": "Fire"},
    {"name": "Magmar", "level": 5, "health": 40, "moves": [ember, smokescreen], "type": "Fire"},
    {"name": "Mudkip", "level": 4, "health": 40, "moves": [water_gun, tackle], "type": "Water"},
    {"name": "Piplup", "level": 5, "health": 45, "moves": [water_gun, peck], "type": "Water"},
    {"name": "Simisage", "level": 5, "health": 45, "moves": [vine_whip, bite], "type": "Grass"}
]

gym_pokemon = [
    {"name": "Charizard", "level": 10, "health": 100, "moves": [flamethrower,ember, scratch,smokescreen], "type": "Fire"},
    {"name": "Blastoise", "level": 10, "health": 100, "moves": [hydro_pump,water_gun ,tackle,smokescreen], "type": "Water"},
    {"name": "Venasaur", "level": 10, "health": 100, "moves": [solar_beam, vine_whip, tackle,smokescreen], "type": "Grass"}
]

starters = {
    "Charmander": Pokemon("Charmander", level=5,experience = 0, health=45, pokemon_type="Fire", moves=[scratch]),
    "Squirtle": Pokemon("Squirtle", level=5,experience =0, health=50, pokemon_type="Water", moves=[tackle]),
    "Bulbasaur": Pokemon("Bulbasaur", level=5,experience =0, health=55, pokemon_type="Grass", moves=[tackle])
}

def encounter_pokemon():
    return random.choice(possible_pokemon)

