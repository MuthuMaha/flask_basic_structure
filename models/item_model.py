from .base_model import BaseModel
from . import db

class Item(BaseModel):
    __tablename__ = 'items'

    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

def get_all_items():
    return Item.query.all()

def get_item(item_id):
    return Item.query.get(item_id)

def create_item(name, price):
    item = Item(name=name, price=price)
    item.save()
    return item

def update_item(item_id, name, price):
    item = Item.query.get(item_id)
    if item:
        item.name = name
        item.price = price
        item.save()

def delete_item(item_id):
    item = Item.query.get(item_id)
    if item:
        item.delete()