from flask import abort, request
from ..app import app
from .controllers import get_players, add_player, get_achievements_byID, get_players_byID, get_statistics_byID, update_player_satistics, delete_player

@app.route('/player', methods=['GET', 'POST'])
def list_players():
    if request.method == 'GET':
        return get_players()
    if request.method == 'POST':
        return add_player()
    else:
        abort (404, description = "Method is not allowed")

@app.route('/player/<int:id>', methods = ['GET', 'DELETE'])
def list_dlt_players_byID(id):
    if request.method == 'GET':
        return get_players_byID(id)
    if request.method == 'DELETE':
        return delete_player(id)
    else:
        abort (404, description = "Method is not allowed")

@app.route('/statistics/<int:id>', methods = ['GET', 'PUT'])
def list_mdf_statistics_byID(id):
    if request.method == 'GET':
        return get_statistics_byID(id)
    if request.method == 'PUT':
        return update_player_satistics(id)
    else:
        abort (404, description = "Method is not allowed")

@app.route('/achievements/<int:id>', methods = ['GET'])
def list_achievements_byID(id):
        return get_statistics_byID(id)