from flask import Flask, jsonify, render_template, request
import httplib
import json

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('league.html')

@app.route('/PremierLeague', methods=['GET','POST'])
def show_prem():
    connection = httplib.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': 'e37416cfe0114dc7b17289f66f61348d', 'X-Response-Control': 'minified'}
    connection.request('GET', '/v1/competitions/426/leagueTable', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    teamnames = [r['team'] for r in response['standing']]
    points = [r['points'] for r in response['standing']]
    played_games = [r['playedGames'] for r in response['standing']]
    goals_for = [r['goals'] for r in response['standing']]
    goals_a = [r['goalsAgainst'] for r in response['standing']]
    return render_template('other.html', data=zip(teamnames, points, played_games, goals_for, goals_a))

@app.route('/DutchLeague', methods=['GET','POST'])
def show_dutch():
    connection = httplib.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': 'e37416cfe0114dc7b17289f66f61348d', 'X-Response-Control': 'minified'}
    connection.request('GET', '/v1/competitions/433/leagueTable', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    teamnames = [r['team'] for r in response['standing']]
    points = [r['points'] for r in response['standing']]
    played_games = [r['playedGames'] for r in response['standing']]
    goals_for = [r['goals'] for r in response['standing']]
    goals_a = [r['goalsAgainst'] for r in response['standing']]
    return render_template('other.html', data=zip(teamnames, points, played_games, goals_for, goals_a))

@app.route('/FrenchLeague', methods=['GET','POST'])
def show_french():
    connection = httplib.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': 'e37416cfe0114dc7b17289f66f61348d', 'X-Response-Control': 'minified'}
    connection.request('GET', '/v1/competitions/434/leagueTable', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    teamnames = [r['team'] for r in response['standing']]
    points = [r['points'] for r in response['standing']]
    played_games = [r['playedGames'] for r in response['standing']]
    goals_for = [r['goals'] for r in response['standing']]
    goals_a = [r['goalsAgainst'] for r in response['standing']]
    return render_template('other.html', data=zip(teamnames, points, played_games, goals_for, goals_a))

@app.route('/ItalianLeague', methods=['GET','POST'])
def show_italy():
    connection = httplib.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': 'e37416cfe0114dc7b17289f66f61348d', 'X-Response-Control': 'minified'}
    connection.request('GET', '/v1/competitions/438/leagueTable', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    teamnames = [r['team'] for r in response['standing']]
    points = [r['points'] for r in response['standing']]
    played_games = [r['playedGames'] for r in response['standing']]
    goals_for = [r['goals'] for r in response['standing']]
    goals_a = [r['goalsAgainst'] for r in response['standing']]
    return render_template('other.html', data=zip(teamnames, points, played_games, goals_for, goals_a))

@app.route('/PortugeseLeague', methods=['GET','POST'])
def show_portugal():
    connection = httplib.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': 'e37416cfe0114dc7b17289f66f61348d', 'X-Response-Control': 'minified'}
    connection.request('GET', '/v1/competitions/439/leagueTable', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    teamnames = [r['team'] for r in response['standing']]
    points = [r['points'] for r in response['standing']]
    played_games = [r['playedGames'] for r in response['standing']]
    goals_for = [r['goals'] for r in response['standing']]
    goals_a = [r['goalsAgainst'] for r in response['standing']]
    return render_template('other.html', data=zip(teamnames, points, played_games, goals_for, goals_a))

if __name__ == '__main__':
    app.run(debug=True)