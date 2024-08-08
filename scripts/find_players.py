import re
import json
from nba_api.stats.library.data import players

# Constants for player data
player_index_id = 0
player_index_full_name = 1
player_index_first_name = 2
player_index_last_name = 3
player_index_is_active = 4

def _find_players(regex_pattern, row_id, players=players):
    """
    Find players based on a regex pattern for a specific row.
    
    :param regex_pattern: Regex pattern to search
    :param row_id: Column index to search in
    :param players: List of players to search
    :return: List of player dictionaries
    """
    players_found = []
    for player in players:
        if re.search(regex_pattern, str(player[row_id]), flags=re.I):
            players_found.append(_get_player_dict(player))
    return players_found

def _get_player_dict(player_row):
    """
    Convert player data row into a dictionary.
    
    :param player_row: List of player data
    :return: Dictionary with player details
    """
    return {
        "id": player_row[player_index_id],
        "full_name": player_row[player_index_full_name],
        "first_name": player_row[player_index_first_name],
        "last_name": player_row[player_index_last_name],
        "is_active": player_row[player_index_is_active],
    }

def find_players_by_first_name(regex_pattern):
    """
    Find players by their first name.
    
    :param regex_pattern: Regex pattern to search for player first names
    :return: List of player dictionaries
    """
    return _find_players(regex_pattern, player_index_first_name)

def save_players_to_json(players, filename='players.json'):
    """
    Save the list of player dictionaries to a JSON file.
    
    :param players: List of player dictionaries
    :param filename: Filename for the JSON output
    """
    with open(filename, 'w') as f:
        json.dump(players, f, indent=4)

def normalize_name(name):
    """Normalize name by removing extra spaces and converting to lowercase."""
    return ' '.join(name.strip().lower().split())

def find_player_id_by_name(player_name):
    """Find player ID by matching first name, last name, or full name."""
    normalized_name = normalize_name(player_name)
    regex_pattern = re.compile(re.escape(normalized_name), re.IGNORECASE)
    
    for player in players:
        full_name = normalize_name(player[player_index_full_name])
        first_name = normalize_name(player[player_index_first_name])
        last_name = normalize_name(player[player_index_last_name])
        
        if regex_pattern.search(full_name) or regex_pattern.search(first_name) or regex_pattern.search(last_name):
            return player[player_index_id]
    
    return None

def main():
    """Main function to interact with the user."""
    player_name = input("Enter the player's first name, last name, or full name: ")
    player_id = find_player_id_by_name(player_name)
    
    if player_id:
        print(f"The ID for '{player_name}' is {player_id}.")
    else:
        print(f"No player found with the name '{player_name}'.")

if __name__ == "__main__":
    main()