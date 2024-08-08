from flask import Blueprint, render_template, request
import pandas as pd
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/player', methods=['GET', 'POST'])
def player():
    if request.method == 'POST':
        player_name = request.form.get('player_name')
        player_id = get_player_id(player_name)
        if player_id:
            # Fetch player stats here
            stats = fetch_player_stats(player_id)
            return render_template('player_basic_stats.html', stats=stats)
    return render_template('player_form.html')

@main.route('/compare', methods=['GET', 'POST'])
def compare():
    if request.method == 'POST':
        player1_name = request.form.get('player1_name')
        player2_name = request.form.get('player2_name')
        player1_id = get_player_id(player1_name)
        player2_id = get_player_id(player2_name)
        if player1_id and player2_id:
            # Fetch stats for both players
            stats1 = fetch_player_stats(player1_id)
            stats2 = fetch_player_stats(player2_id)
            return render_template('compare_basic_stats.html', stats1=stats1, stats2=stats2)
    return render_template('compare_form.html')

def get_player_id(name):
    players_list = players.get_players()
    player = next((player for player in players_list if player['full_name'] == name), None)
    return player['id'] if player else None

def fetch_player_stats(player_id):
    stats = playercareerstats.PlayerCareerStats(player_id=player_id).get_data_frames()[0]
    return stats
