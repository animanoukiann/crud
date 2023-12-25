from sqlalchemy import inspect, ForeignKey
from sqlalchemy.orm import validates, relationship

from .. import db

class Player(db.Model):
    __tablename__ = 'player'

    id          = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    name        = db.Column(db.String(255), nullable=False)
    nationality = db.Column(db.String(255), nullable=False)
    position    = db.Column(db.String(255), nullable=False)
    age         = db.Column(db.Integer, nullable=False)
    transfer_y  = db.Column(db.Integer, nullable=False)
    
    achievements    = relationship('Achievements', backref='player', lazy=True)
    statistics      = relationship('Statistics', backref='player', lazy=True)

class Achievements(db.Model):
    __tablename__ = 'achievements'

    id          = db.Column(db.Integer, ForeignKey('player.id'))
    squad_n     = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    ballon_dor  = db.Column(db.Integer)
    champ_liga  = db.Column(db.Integer)
    eurp_liga   = db.Column(db.Integer)
    cp_del_rey  = db.Column(db.Integer)
    spc_de_esp  = db.Column(db.Integer)

class Statistics(db.Model):
    __tablename__ = 'statistics'

    id          = db.Column(db.Integer, ForeignKey('player.id'))
    prfrmanc_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    goals       = db.Column(db.Integer)
    assists     = db.Column(db.Integer)
    yellow_c    = db.Column(db.Integer)
    red_c       = db.Column(db.Integer)
    injury      = db.Column(db.String(255))

@validates('name', 'nationality', 'position', 'age', 'transfer_y')
def empty_string_to_null(self, key, value):
    if value == '':
        return None
    return value

def to_dict(self):
    column_attrs = inspect(self).mapper.column_attrs
    return {c.key: getattr(self, c.key) for c in column_attrs}
