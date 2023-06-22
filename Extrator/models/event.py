from core.configs import session
from sqlalchemy import text
import json


def events():
    
    result = session.execute(text('SELECT room_id, type FROM events;'))
    for row in result:
        continue