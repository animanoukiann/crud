from sqlalchemy import func
from flask import request, jsonify
from .. import db
from .models import Player, Statistics, Achievements

def get_players():
    player = Player.query.all()
    response = []
    for i in player:
        response.append(player.to_dict())
    return jsonify(response)

def add_player():
    request_form = request.form.to_dict()
    last_id = db.session.query(func.max(Player.id)).scalar() or 0
    squad_n = db.session.query(func.max(Achievements.squad_n)).scalar() or 0
    id = last_id + 1
    prfrmanc_id = id

    new_player = Player(
        id          = id,
        name        = request_form['name'],
        nationality = request_form['nationality'],
        position    = request_form['position'],
        age         = request_form['age'],
        transfer_y  = request_form['transfer_y'],
        )
    new_achievements = Achievements(
        id          = new_player.id,
        squad_n     = squad_n,
        ballon_dor  = request_form['ballon_dor'],
        champ_liga  = request_form['champ_liga'],
        eurp_liga   = request_form['eurp_liga'],
        cp_del_rey  = request_form['cp_del_rey'],
        spc_de_esp  = request_form['spc_de_esp']
    )
    new_statistics = Statistics(
        id          = new_player.id,
        prfrmanc_id = prfrmanc_id,
        goals       = request_form['goals'],
        assists     = request_form['assists'],
        yellow_c    = request_form['yellow_c'],
        red_c       = request_form['red_c'],
        injury      = request_form['injury']
    )

    db.sessio.add(new_statistics)
    db.session.add(new_achievements)
    db.session.add(new_player)
    db.session.commit()

    response_player       = Player.query.get(id).toDict() 
    response_achievements = Achievements.query.filter_by(id=id).first().toDict()
    response_statistics   = Statistics.query.filter_by(id=id).first().toDict()
    
    response = {
        "player": response_player,
        "achievements": response_achievements,
        "statistics": response_statistics
    }

    return jsonify(response)

def get_players_byID(id):
    response = Player.query.get(id).toDict()
    return jsonify(response)

def get_achievements_byID(id):
    response = Achievements.query.get(id).toDict()
    return jsonify(response)

def get_statistics_byID(id):
    response = Statistics.query.get(id).toDict()
    return jsonify(response)

def update_player_satistics(id):
    request_form = request.form.to_dict()
    player = Statistics.query.get(id)

    player.goals        = request_form['goals']
    player.assists      = request_form['assists']
    player.yellow_c     = request_form['yellow_c']
    player.red_c        = request_form['red_c']
    player.injury       = request_form['injury']
    db.session.commit()

    response = Statistics.query.get(id).toDict()
    return jsonify(response)

def delete_player(id):
    Player.query.filter_by(id=id).delete()
    Statistics.query.filter_by(id=id).delete()
    Achievements.query.filter_by(id=id).delete()
    db.session.commit()


