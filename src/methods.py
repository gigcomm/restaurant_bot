from src.config import *
from models import *

def getall_food_group():
    Session = sessionmaker(bind = engine)
    session = Session()

    results = session.query(food_groups).all()
    session.close()

    return results


def getall_orders():
    Session = sessionmaker(bind = engine)
    session = Session()

    results = session.query(orders).all()
    session.close()

    return results


def getall_ad_cods():
    Session = sessionmaker(bind = engine)
    session = Session()

    results = session.query(ad_cods).all()
    session.close()

    return results


def getall_client():
    Session = sessionmaker(bind = engine)
    session = Session()

    results = session.query(client).all()
    session.close()

    return results


def getall_menu():
    Session = sessionmaker(bind = engine)
    session = Session()

    results = session.query(menu).all()
    session.close()

    return results


def getall_orders_menu():
    Session = sessionmaker(bind = engine)
    session = Session()

    results = session.query(orders_menu).all()
    session.close()

    return results


def getall_restaurant():
    Session = sessionmaker(bind = engine)
    session = Session()

    results = session.query(restaurant).all()
    session.close()

    return results


def getall_status():
    Session = sessionmaker(bind = engine)
    session = Session()

    results = session.query(status).all()
    session.close()

    return results


def menu_delete(name_str):
    Session = sessionmaker(bind = engine)
    session = Session()

    pos_to_delete = session.query(menu).filter(menu.name == name_str).first()
    session.delete(pos_to_delete)
    session.commit()

    session.close()


def menu_upd_price(name_str, new_price):
    Session = sessionmaker(bind = engine)
    session = Session()

    price_upd = session.query(menu).filter(menu.name==name_str).first()
    price_upd.price = new_price
    session.commit()

    session.close()


def menu_upd_name(name_str, new_name):
    Session = sessionmaker(bind = engine)
    session = Session()

    name_upd = session.query(menu).filter(menu.name==name_str).first()
    name_upd.name = new_name
    session.commit()

    session.close()


def menu_upd_description(name_str, new_desc):
    Session = sessionmaker(bind = engine)
    session = Session()

    desc_upd = session.query(menu).filter(menu.name==name_str).first()
    desc_upd.description = new_desc
    session.commit()

    session.close()


def menu_upd_pic(name_str, new_pic):
    Session = sessionmaker(bind = engine)
    session = Session()

    pic_upd = session.query(menu).filter(menu.name==name_str).first()
    pic_upd.pic = new_pic
    session.commit()

    session.close()


def order_upd_status(fid, new_status):
    Session = sessionmaker(bind = engine)
    session = Session()

    status_upd = session.query(orders).filter(orders.id==fid).first()
    match new_status:
        case 'Оплачен':
            status_upd.status = 1
        case 'Ожидает оплаты':
            status_upd.status = 2
        case 'Отменён':
            status_upd.status = 3

    session.commit()
    session.close()


def get_orders():
    Session = sessionmaker(bind = engine)
    session = Session()

    results = session.query(orders, orders_menu, menu).join(orders_menu, orders_menu.fk_fk_order == orders.id).join(menu, orders_menu.fk_fk_menu == menu.id).all()

    session.close()
    return results