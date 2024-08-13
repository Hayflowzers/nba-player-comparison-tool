from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.utils import get_player_stats, compare_players_stats

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/one_player')
def one_player():
    return render_template('player_form.html')

@main.route('/two_players')
def two_players():
    return render_template('compare_form.html')

@main.route('/player_basic_stats', methods=['POST'])
def player_basic_stats():
    player_name = request.form['player_name']
    if player_name:
        stats = get_player_stats(player_name, stats_type='basic')
        if stats:
            return render_template('player_basic_stats.html', player_name=player_name, stats=stats)
        else:
            flash(f"No stats found for {player_name}.")
    else:
        flash("Please enter a player name.")
    return redirect(url_for('main.one_player'))

@main.route('/player_advanced_stats', methods=['POST'])
def player_advanced_stats():
    player_name = request.form['player_name']
    if player_name:
        stats = get_player_stats(player_name, stats_type='advanced')
        if stats:
            return render_template('player_advanced_stats.html', player_name=player_name, stats=stats)
        else:
            flash(f"No stats found for {player_name}.")
    else:
        flash("Please enter a player name.")
    return redirect(url_for('main.one_player'))

@main.route('/compare_basic_stats', methods=['POST'])
def compare_basic_stats():
    player1_name = request.form['player1_name']
    player2_name = request.form['player2_name']
    if player1_name and player2_name:
        stats = compare_players_stats(player1_name, player2_name, stats_type='basic')
        if stats:
            return render_template('compare_basic_stats.html', player1_name=player1_name, player2_name=player2_name, stats=stats)
        else:
            flash(f"No stats found for {player1_name} or {player2_name}.")
    else:
        flash("Please enter both player names.")
    return redirect(url_for('main.two_players'))

@main.route('/compare_advanced_stats', methods=['POST'])
def compare_advanced_stats():
    player1_name = request.form['player1_name']
    player2_name = request.form['player2_name']
    if player1_name and player2_name:
        stats = compare_players_stats(player1_name, player2_name, stats_type='advanced')
        if stats:
            return render_template('compare_advanced_stats.html', player1_name=player1_name, player2_name=player2_name, stats=stats)
        else:
            flash(f"No stats found for {player1_name} or {player2_name}.")
    else:
        flash("Please enter both player names.")
    return redirect(url_for('main.two_players'))

