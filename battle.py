import random
import time

def battle(player_pokemon, wild_pokemon):
    
    while player_pokemon.is_alive() and wild_pokemon.is_alive():
        # Player's turn
        print(f"\nYour {player_pokemon.name} HP: {player_pokemon.health}")
        print(f"Wild {wild_pokemon.name} HP: {wild_pokemon.health}")

        # Display moves
        print("Choose your move:")
        for idx, move in enumerate(player_pokemon.moves):
            print(f"{idx + 1}. {move.name} POWER={move.damage}")
        
        try:
            move_choice = int(input("Select move (1-4): ")) - 1
            if move_choice < 0 or move_choice >= len(player_pokemon.moves):
                print("Invalid choice. Try again.")
                continue
            move = player_pokemon.moves[move_choice]
        except ValueError:
            print("Invalid input. Please choose a valid move.")
            continue

        # Player attacks
        if random.random() > 0.2:
            player_pokemon.attack(wild_pokemon,move)
        else:
            print("attack missed!")

        if not wild_pokemon.is_alive():
            print(f"{wild_pokemon.name} fainted!")
            break

        # Wild Pokémon's turn (random move)
        wild_move = random.choice(wild_pokemon.moves)
        if random.random() > 0.35:
            wild_pokemon.attack(player_pokemon,wild_move)
        else:
            print("attack missed!")
        

        if not player_pokemon.is_alive():
            print(f"{player_pokemon.name} fainted!")
            break

    if player_pokemon.is_alive():
        print(f"{player_pokemon.name} won the battle!")
        player_pokemon.experience +=10
        if player_pokemon.experience >= 20:
            player_pokemon.level_up()
        time.sleep(6) 
        return "W"
    else:
        print(f"{player_pokemon.name} lost the battle.")
        return "L"