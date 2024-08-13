import re
from nba_api.stats.library.data import players
from nba_api.stats.endpoints import playercareerstats

# Constants for player data
player_index_id = 0
player_index_full_name = 1
player_index_first_name = 2
player_index_last_name = 3
player_index_is_active = 4

def _find_players(regex_pattern, row_id, players=players):
    players_found = []
    for player in players:
        if re.search(regex_pattern, str(player[row_id]), flags=re.I):
            players_found.append(_get_player_dict(player))
    return players_found

def _get_player_dict(player_row):
    return {
        "id": player_row[player_index_id],
        "full_name": player_row[player_index_full_name],
        "first_name": player_row[player_index_first_name],
        "last_name": player_row[player_index_last_name],
        "is_active": player_row[player_index_is_active],
    }

def find_player_id_by_name(player_name):
    normalized_name = normalize_name(player_name)
    regex_pattern = re.compile(re.escape(normalized_name), re.IGNORECASE)
    
    for player in players:
        full_name = normalize_name(player[player_index_full_name])
        first_name = normalize_name(player[player_index_first_name])
        last_name = normalize_name(player[player_index_last_name])
        
        if regex_pattern.search(full_name) or regex_pattern.search(first_name) or regex_pattern.search(last_name):
            return player[player_index_id]
    
    return None

def normalize_name(name):
    """Normalize name by removing extra spaces and converting to lowercase."""
    return ' '.join(name.strip().lower().split())

def get_player_stats(player_id):
    """Retrieve and display basic player stats."""
    career = playercareerstats.PlayerCareerStats(player_id=player_id, per_mode36="PerGame")
    career_stats = career.get_data_frames()[0]
    
    # Get the latest season's per-game stats
    if not career_stats.empty:
        latest_season_stats = career_stats.iloc[-1]  # Get the most recent season's stats
        
        ppg = latest_season_stats['PTS']
        apg = latest_season_stats['AST']
        gp = latest_season_stats['GP']
        
    else:
        ppg = 0
        apg = 0
        gp = 0
    
    stats = {
        "Games Played": gp,
        "Points Per Game": round(ppg, 2),
        "Assists Per Game": round(apg, 2)
    }
    
    return stats

def main():
    player_name = input("Enter the player's first name, last name, or full name: ")
    player_id = find_player_id_by_name(player_name)
    
    if player_id:
        print(f"The ID for '{player_name}' is {player_id}.")
        
        # Get and display player stats
        stats = get_player_stats(player_id)
        print("Basic Player Stats:")
        for key, value in stats.items():
            print(f"{key}: {value}")
        
    else:
        print(f"No player found with the name '{player_name}'.")

if __name__ == "__main__":
    main()

