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

    # Calculate career totals and averages
    career_totals = career_stats.sum()
    total_games = career_totals['GP']

    if stats_type == 'basic':
        stats = {
            'GP': int(total_games),
            'Points Per Game': round(career_totals['PTS'] / total_games, 1) if total_games else 0,
            'Assists Per Game': round(career_totals['AST'] / total_games, 1) if total_games else 0,
            'Rebounds Per Game': round(career_totals['REB'] / total_games, 1) if total_games else 0,
            'Steals Per Game': round(career_totals['STL'] / total_games, 1) if total_games else 0,
            'Blocks Per Game': round(career_totals['BLK'] / total_games, 1) if total_games else 0,
            'Turnovers Per Game': round(career_totals['TOV'] / total_games, 1) if total_games else 0,
            'Field Goal Percentage': round(career_totals['FGM'] / career_totals['FGA'] * 100, 1) if career_totals['FGA'] else 0,
            'Three-Point Percentage': round(career_totals['FG3M'] / career_totals['FG3A'] * 100, 1) if career_totals['FG3A'] else 0,
            'Free Throw Percentage': round(career_totals['FTM'] / career_totals['FTA'] * 100, 1) if career_totals['FTA'] else 0,
        }
    elif stats_type == 'advanced':
        latest_season_stats = career_stats.iloc[-1]
        stats = {
            'Player Efficiency Rating': round(latest_season_stats.get('PER', 0), 1),
            'True Shooting Percentage': round(latest_season_stats.get('TS_PCT', 0) * 100, 1),  # Assuming TS_PCT is in decimal form
            'Box Plus/Minus': round(latest_season_stats.get('BPM', 0), 1),
            'Value Over Replacement Player': round(latest_season_stats.get('VORP', 0), 1),
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
                'GP': int(total_games1),
                'Points Per Game': round(player1_stats['PTS'] / total_games1, 1) if total_games1 else 0,
                'Assists Per Game': round(player1_stats['AST'] / total_games1, 1) if total_games1 else 0,
                'Rebounds Per Game': round(player1_stats['REB'] / total_games1, 1) if total_games1 else 0,
                'Steals Per Game': round(player1_stats['STL'] / total_games1, 1) if total_games1 else 0,
                'Blocks Per Game': round(player1_stats['BLK'] / total_games1, 1) if total_games1 else 0,
                'Turnovers Per Game': round(player1_stats['TOV'] / total_games1, 1) if total_games1 else 0,
                'Field Goal Percentage': round(player1_stats['FGM'] / player1_stats['FGA'] * 100, 1) if player1_stats['FGA'] else 0,
                'Three-Point Percentage': round(player1_stats['FG3M'] / player1_stats['FG3A'] * 100, 1) if player1_stats['FG3A'] else 0,
                'Free Throw Percentage': round(player1_stats['FTM'] / player1_stats['FTA'] * 100, 1) if player1_stats['FTA'] else 0,
            },
            player2_name: {
                'GP': int(total_games2),
                'Points Per Game': round(player2_stats['PTS'] / total_games2, 1) if total_games2 else 0,
                'Assists Per Game': round(player2_stats['AST'] / total_games2, 1) if total_games2 else 0,
                'Rebounds Per Game': round(player2_stats['REB'] / total_games2, 1) if total_games2 else 0,
                'Steals Per Game': round(player2_stats['STL'] / total_games2, 1) if total_games2 else 0,
                'Blocks Per Game': round(player2_stats['BLK'] / total_games2, 1) if total_games2 else 0,
                'Turnovers Per Game': round(player2_stats['TOV'] / total_games2, 1) if total_games2 else 0,
                'Field Goal Percentage': round(player2_stats['FGM'] / player2_stats['FGA'] * 100, 1) if player2_stats['FGA'] else 0,
                'Three-Point Percentage': round(player2_stats['FG3M'] / player2_stats['FG3A'] * 100, 1) if player2_stats['FG3A'] else 0,
                'Free Throw Percentage': round(player2_stats['FTM'] / player2_stats['FTA'] * 100, 1) if player2_stats['FTA'] else 0,
            }
        }
    elif stats_type == 'advanced':
        player1_latest = player1_career.get_data_frames()[0].iloc[-1]
        player2_latest = player2_career.get_data_frames()[0].iloc[-1]
        stats = {
            player1_name: {
                'Player Efficiency Rating': round(player1_latest.get('PER', 0), 1),
                'True Shooting Percentage': round(player1_latest.get('TS_PCT', 0) * 100, 1),  # Assuming TS_PCT is in decimal form
                'Box Plus/Minus': round(player1_latest.get('BPM', 0), 1),
                'Value Over Replacement Player': round(player1_latest.get('VORP', 0), 1),
            },
            player2_name: {
                'Player Efficiency Rating': round(player2_latest.get('PER', 0), 1),
                'True Shooting Percentage': round(player2_latest.get('TS_PCT', 0) * 100, 1),  # Assuming TS_PCT is in decimal form
                'Box Plus/Minus': round(player2_latest.get('BPM', 0), 1),
                'Value Over Replacement Player': round(player2_latest.get('VORP', 0), 1),
            }
        }
    else:
        return None
    
    return stats
