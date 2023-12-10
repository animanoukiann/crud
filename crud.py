from flask import Flask, jsonify, request, abort

app = Flask(__name__)

players = [
    {
        "Name": "Karim Benzema",
        "Nationality": "French",
        "Position": "Forward",
        "Age": 36,
        "Transfer_Year": 2009,
    },
    {
        "Name": "Thibaut Courtois",
        "Nationality": "Belgian",
        "Position": "Goalkeeper",
        "Age": 31,
        "Transfer_Year": 2018,
    },
    {
        "Name": "Lucas Vazquez",
        "Nationality": "Spanish",
        "Position": "Midfielder",
        "Age": 32,
        "Transfer_Year": 2015,
    },
    {
        "Name": "Nacho",
        "Nationality": "Spanish",
        "Position": "Defender",
        "Age": 33,
        "Transfer_Year": 2001,
    },
    {
        "Name": "Dani Carvajal",
        "Nationality": "Spanish",
        "Position": "Defender",
        "Age": 31,
        "Transfer_Year": 2013,
    },
    {
        "Name": "Federico Valverde",
        "Nationality": "Uruguayan",
        "Position": "Midfielder",
        "Age": 25,
        "Transfer_Year": 2015,
    }
]

@app.route('/players', methods = ['GET'])
def get_players():
    return players

@app.route('/players/<int:transfer_year>', methods = ['GET'])
def get_ty_players(transfer_year):
    arr = []
    for player in players:
        if transfer_year == player['Transfer_Year']:
            arr.append(player['Name'])
    if not arr:
        return "No one transfered in that year"
    return arr

@app.route('/players', methods = ['POST'])
def add_player():
    new_player = {'name':request.json['Name'], 'nat':request.json['Nationality'],
                   'pos':request.json['Position'], 'age':request.json['Age'],
                   'transfer_year':request.json['Transfer_Year']}
    players.append(new_player)
    return new_player["name"]

@app.route('/players/<int:transfer_year>', methods=['PUT'])
def update_player(transfer_year):
    for player in players:
        if transfer_year == player["Transfer_Year"]:
            player['Position'] = request.json['Position']
            return player['Name']
    abort (404, description = "No one transfered in that year")

@app.route('/players/<int:transfer_year>', methods = ['DELETE'])
def del_player(transfer_year):
    for player in players:
        if player['Transfer_Year'] == transfer_year:
            players.remove(player)
            return "Player transfered to other club"
    abort (404, description = "No one transfered in that year")

if __name__ == '__main__':
    app.run(debug=True)