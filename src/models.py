from sqlalchemy import Column, Integer, String, Date, ForeignKey, BLOB
from src.config import Base


class food_groups(Base):
    __tablename__ = 'food_groups'

    id = Column(Integer, primary_key=True)
    group_name = Column(String)


class orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    order_adress = Column(String)
    order_date = Column(Date)
    price = Column(Integer)
    status = Column(Integer, ForeignKey('status.id'))

class client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    adress = Column(String)
    fk_client_order = Column(Integer, ForeignKey('orders.id'))


class ad_cods(Base):
    __tablename__ = 'ad_cods'
    id = Column(Integer, primary_key=True)
    cod = Column(Integer)


class menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    pic = Column(BLOB)
    fk_menu_group = Column(Integer, ForeignKey(food_groups.id))


class orders_menu(Base):
    __tablename__ = 'orders_menu'
    fk_fk_order = Column(Integer, ForeignKey('orders.id'))
    fk_fk_menu = Column(Integer, ForeignKey('menu.id'))
    count_in_menu = Column(Integer)
    id = Column(Integer, primary_key=True)


class status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    status_name = Column(String)


class restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    adress = Column(String)
    fk_restaurant_menu = Column(Integer, ForeignKey('menu.id'))
    fk_restaurant_client = Column(Integer, ForeignKey('client.id'))
    fk_restaurant_adcods = Column(Integer, ForeignKey('ad_cods.id'))

