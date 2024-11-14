import map
import pokemon
import battle
import os
import random
import time

def rules():
    print("\nRULES")
    print("Use W A S D to move")
    print("Beat the gym leader")
    print("Your pokemon should not faint")
    print("Earn Exp and level up by fighting wild pokemon in grass")
    print("Walk on yellow path to not encounter any wild pokemon")
    print("Visit your house to heal pokemon")
    print("Take decisions wisely! Remember type advantage!")
    print("GENERATING NEW WORLD!",end='')
    for i in range(5):
        print('.',end='')
        time.sleep(0.5)

def start_menu():
    print("Welcome to the Pokémon World!")
    player_name = input("What's your name, Trainer? ").strip()
    
    # Choose starter Pokémon
    print("\nChoose your starter Pokémon:")
    print("1. Charmander (Fire Type)")
    print("2. Squirtle (Water Type)")
    print("3. Bulbasaur (Grass Type)")
    
    while True:
        choice = input("Enter 1, 2, or 3 to select your starter: ")
        if choice == "1":
            player_pokemon = pokemon.starters["Charmander"]
            break
        elif choice == "2":
            player_pokemon = pokemon.starters["Squirtle"]
            break
        elif choice == "3":
            player_pokemon = pokemon.starters["Bulbasaur"]
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    
    print(f"\nGreat choice, {player_name}! You chose {player_pokemon.name}!")
    print(f"{player_pokemon.name} is a level {player_pokemon.level} {player_pokemon.pokemon_type} type with the following moves:")
    for move in player_pokemon.moves:
        print(f"- {move.name} (Damage: {move.damage})")

    return player_name, player_pokemon


def game_loop(map_data,spawn,player_pokemon,gym_type): 
    player_pos = spawn
    prev = map.place_player(map_data,player_pos)
    
    while True:
        # Display map with the player
        os.system("cls") 
        map.display_map(map_data)

        # Get user input
        print("Move (WASD): ", end='', flush=True)
        move = map.get_key()  
        print(move)
        if move in ('W', 'A', 'S', 'D'):
            # Update player position
            new_position = map.move_player(player_pos, move)
            map.remove_player(map_data,player_pos,prev)
            player_pos[0], player_pos[1] = new_position
            prev = map.place_player(map_data,player_pos)
        else:
            print("Invalid move. Use W, A, S, or D.")
            time.sleep(1)
        
        if prev == map.terrain["grass"]:
            if random.random() < 0.5:
                print("A wild Pokémon has appeared!")
                wild_pokemon_data = pokemon.encounter_pokemon()
                print(f"You encountered a wild {wild_pokemon_data['name']}!")
                print(f"Level: {wild_pokemon_data['level']}, Health: {wild_pokemon_data['health']}")
                print(f"Moves: {', '.join([str(i) for i in wild_pokemon_data['moves']])}")

                while True:
                    response = input("Do you want to fight(y/n)? :").lower()
                    if response in ['y','n']:
                        if response == 'y':
                            print("Prepare for battle!")
                            wild_pokemon = pokemon.Pokemon(wild_pokemon_data["name"], wild_pokemon_data["level"],0, wild_pokemon_data["health"], wild_pokemon_data["moves"], wild_pokemon_data["type"])
                            battle_result = battle.battle(player_pokemon, wild_pokemon)
                            if battle_result == 'L':
                                print("GAME OVER! :(")
                                time.sleep(6)
                                return
                            break
                        else:
                            break

            else:
                pass

        elif prev == map.terrain["house"]:
            print("Pokemon healed fully!")
            player_pokemon.health = player_pokemon.max_health
            time.sleep(2)

        elif prev == map.terrain["gym"]:
            print("You entered the gym...")
            while True:
                    gym_pokemon_data = pokemon.gym_pokemon[gym_type]
                    print(f"Gym Leader has a {gym_pokemon_data['name']}!")
                    print(f"Level: {gym_pokemon_data['level']}, Health: {gym_pokemon_data['health']}")
                    print(f"Moves: {', '.join([str(i) for i in gym_pokemon_data['moves']])}")
                    response = input("Are you ready to challenge the gym?(y/n)? :").lower()
                    if response in ['y','n']:
                        if response == 'y':
                            print("Prepare for battle!")
                            gym_pokemon = pokemon.Pokemon(gym_pokemon_data["name"], gym_pokemon_data["level"],0, gym_pokemon_data["health"], gym_pokemon_data["moves"], gym_pokemon_data["type"])
                            battle_result = battle.battle(player_pokemon, gym_pokemon)
                            if battle_result == 'L':
                                print("GAME OVER! :'(")
                                time.sleep(6)
                                return
                            
                            elif battle_result == 'W':
                                print("You have beaten the gym leader!!!!!!!!")
                                print("Congragulations!")
                                print("GAME OVER")
                                time.sleep(6)
                                return
                            else:
                                break
                        else:
                            print("You stepped out of gym...")
                            time.sleep(1)
                            break

if __name__ == "__main__":

    player_name, player_pokemon = start_menu()
    rules()
    while True:
        ready = input("\nReady?(click y):").lower()
        if ready == 'y':
            break    
    gym_type = random.randint(0,2)
    map_data = map.create_map()
    map_data,spawn = map.randomize_map(map_data)
    game_loop(map_data,spawn,player_pokemon,gym_type)