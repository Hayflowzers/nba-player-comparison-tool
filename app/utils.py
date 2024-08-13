from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

def get_player_id(player_name):
    """
    Retrieve the player ID based on player name.
    
    :param player_name: Name of the player
    :return: Player ID or None if not found
    """
    player_dict = players.find_players_by_full_name(player_name)
    if player_dict:
        return player_dict[0]['id']
    return None

def get_player_stats(player_name, stats_type='basic'):
    """
    Retrieve stats for a single player using nba_api.
    
    :param player_name: Name of the player to fetch stats for
    :param stats_type: 'basic' or 'advanced'
    :return: Dictionary of stats or None if not found
    """
    player_id = get_player_id(player_name)
    if not player_id:
        return None

    # Fetch player career stats
    career = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_stats = career.get_data_frames()[0]

    # Calculate career averages
    career_totals = career_stats.sum()
    total_games = career_totals['GP']

    if stats_type == 'basic':
        stats = {
            'Points Per Game': career_totals['PTS'] / total_games if total_games else 0,
            'Assists Per Game': career_totals['AST'] / total_games if total_games else 0,
            'Rebounds Per Game': career_totals['REB'] / total_games if total_games else 0,
            # Add other basic stats as needed
        }
    elif stats_type == 'advanced':
        # Example of how advanced stats might be fetched differently
        latest_season_stats = career_stats.iloc[-1]
        stats = {
            'Player Efficiency Rating': latest_season_stats.get('PER', 'N/A'),  # Adjust as needed
            'True Shooting Percentage': latest_season_stats.get('TS_PCT', 'N/A'),  # Adjust as needed
            # Add other advanced stats as needed
        }
    else:
        return None
    
    return stats

def compare_players_stats(player1_name, player2_name, stats_type='basic'):
    """
    Compare stats for two players using nba_api.
    
    :param player1_name: Name of the first player
    :param player2_name: Name of the second player
    :param stats_type: 'basic' or 'advanced'
    :return: Dictionary with both players' stats or None if not found
    """
    player1_id = get_player_id(player1_name)
    player2_id = get_player_id(player2_name)
    
    if not player1_id or not player2_id:
        return None

    # Fetch player career stats
    player1_career = playercareerstats.PlayerCareerStats(player_id=player1_id)
    player2_career = playercareerstats.PlayerCareerStats(player_id=player2_id)

    player1_stats = player1_career.get_data_frames()[0].sum()
    player2_stats = player2_career.get_data_frames()[0].sum()

    total_games1 = player1_stats['GP']
    total_games2 = player2_stats['GP']

    if stats_type == 'basic':
        stats = {
            player1_name: {
                'Points Per Game': player1_stats['PTS'] / total_games1 if total_games1 else 0,
                'Assists Per Game': player1_stats['AST'] / total_games1 if total_games1 else 0,
                'Rebounds Per Game': player1_stats['REB'] / total_games1 if total_games1 else 0,
            },
            player2_name: {
                'Points Per Game': player2_stats['PTS'] / total_games2 if total_games2 else 0,
                'Assists Per Game': player2_stats['AST'] / total_games2 if total_games2 else 0,
                'Rebounds Per Game': player2_stats['REB'] / total_games2 if total_games2 else 0,
            }
        }
    elif stats_type == 'advanced':
        player1_latest = player1_career.get_data_frames()[0].iloc[-1]
        player2_latest = player2_career.get_data_frames()[0].iloc[-1]
        stats = {
            player1_name: {
                'Player Efficiency Rating': player1_latest.get('PER', 'N/A'),
                'True Shooting Percentage': player1_latest.get('TS_PCT', 'N/A'),
            },
            player2_name: {
                'Player Efficiency Rating': player2_latest.get('PER', 'N/A'),
                'True Shooting Percentage': player2_latest.get('TS_PCT', 'N/A'),
            }
        }
    else:
        return None
    
    return stats
