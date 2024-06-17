from models import db

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer,primary_key=True)
    def save(self):
        db.session.add(self)
        db,session.commit()
    
    def delete(self):
        db.session.delete(self)
        db,session.commit()

    def to_dict(self):
        return {c.name:getattr(self, c.name) for c in self.__table__.columns}

    # def __init__(self, **kwargs):
    #     for key,value in kwargs.items():
    #         setattr(self, key, value)
    
    # def __repr__(self):
    #     return f'<{self.__class__.__name__}{self.__dict__}>'