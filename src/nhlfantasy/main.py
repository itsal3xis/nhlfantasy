from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)

# Charger les stats des joueurs
with open("src/nhlfantasy/logic/statistics/playerStats.json", "r") as f:
    players = json.load(f)

def find_player_by_slug(slug):
    # Transforme le nom en slug pour la comparaison
    for player in players:
        name = player.get("name", "")
        if name and slug == name.lower().replace(" ", ""):
            return player
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<slug>')
def profile(slug):
    player = find_player_by_slug(slug)
    if not player:
        return "Player not found", 404

    # Exemple de données à passer au template (à adapter selon ton JSON)
    return render_template(
        'profile.html',
        banner_url=player.get("heroImage", "/static/default_banner.jpg"),
        headshot_url=player.get("headshot", "/static/default_headshot.png"),
        team_logo_url=player.get("teamLogo", "/static/default_team.png"),
        player_number=player.get("sweaterNumber", ""),
        player_name=player.get("name", ""),
        elo=player.get("elo", ""),
        elo_diff=player.get("eloDiff", ""),
        stats_period="Regular Season",
        position=player.get("position", ""),
        games_played=player.get("gamesPlayed", ""),
        goals=player.get("goals", ""),
        assists=player.get("assists", ""),
        comparison_chart_url="/static/comparison_chart.png",  # à remplacer par ton graphique
        opponent_headshot_url="/static/opponent_headshot.png",  # exemple
        opponent_name="Connor Hellebuyck",  # exemple
        opponent_elo="2381"  # exemple
    )

if __name__ == '__main__':
    app.run(debug=True, port=5001)