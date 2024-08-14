from flask import Blueprint, render_template, request, redirect, url_for, flash

from app.utils import get_player_stats, compare_players_stats

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/one_player', methods=['GET', 'POST'])
def one_player():
    if request.method == 'POST':
        player_name = request.form.get('player_name')
        if player_name:
            return redirect(url_for('main.one_player_form', player_name=player_name))
        else:
            flash("Please enter a player name.")
    return render_template('player_name_form.html')

@main.route('/two_players', methods=['GET', 'POST'])
def two_players():
    if request.method == 'POST':
        player1_name = request.form.get('player1_name')
        player2_name = request.form.get('player2_name')
        if player1_name and player2_name:
            return redirect(url_for('main.two_players_form', player1_name=player1_name, player2_name=player2_name))
        else:
            flash("Please enter both player names.")
    return render_template('compare_players_name_form.html')

@main.route('/one_player_form', methods=['GET'])
def one_player_form():
    player_name = request.args.get('player_name')
    if player_name:
        stats = get_player_stats(player_name, stats_type='basic')
        if stats:
            return render_template('player_basic_stats.html', player_name=player_name, stats=stats)
        else:
            flash(f"No stats found for {player_name}.")
    else:
        flash("No player name provided.")
    return redirect(url_for('main.one_player'))


@main.route('/two_players_form', methods=['GET'])
def two_players_form():
    player1_name = request.args.get('player1_name')
    player2_name = request.args.get('player2_name')
    if player1_name and player2_name:
        return render_template('compare_form.html', player1_name=player1_name, player2_name=player2_name)
    else:
        flash("Both player names are required.")
    return redirect(url_for('main.two_players'))


@main.route('/player_basic_stats', methods=['POST'])
def player_basic_stats():
    player_name = request.form.get('player_name')
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
    player_name = request.form.get('player_name')
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
    player1_name = request.form.get('player1_name')
    player2_name = request.form.get('player2_name')
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
    player1_name = request.form.get('player1_name')
    player2_name = request.form.get('player2_name')
    if player1_name and player2_name:
        stats = compare_players_stats(player1_name, player2_name, stats_type='advanced')
        if stats:
            return render_template('compare_advanced_stats.html', player1_name=player1_name, player2_name=player2_name, stats=stats)
        else:
            flash(f"No stats found for {player1_name} or {player2_name}.")
    else:
        flash("Please enter both player names.")
    return redirect(url_for('main.two_players'))
