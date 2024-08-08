import pandas as pd

def get_player_stats(player_name):
    df = pd.read_csv('data/mock_players_stats.csv')  # Use mock data
    player_stats = df[df['player_name'] == player_name]
    if not player_stats.empty:
        return player_stats
    return None

def compare_players_stats(player1_name, player2_name):
    df = pd.read_csv('data/mock_players_stats.csv')  # Use mock data
    player1_stats = df[df['player_name'] == player1_name]
    player2_stats = df[df['player_name'] == player2_name]
    return player1_stats, player2_stats
