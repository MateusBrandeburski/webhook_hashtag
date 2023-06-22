from core.configs import session
from sqlalchemy import text
import json


def event_json():
    
    result = session.execute(text('SELECT json FROM event_json;'))

    for row in result:
        json_data = row[0] 
        row = json.loads(json_data)

        type = row['type']
        room_id = row['room_id']
        sender = row['sender']
        depth = row['depth']
        state_key = row['state_key'] if 'state_key' in row else None
        origin = row['origin']
        origin_server_ts = row['origin_server_ts']
        rom_version = row['content']['room_version'] if 'room_version' in row['content'] else None
        creator = row['content']['creator'] if 'creator' in row['content'] else None
        displayname = row['content']['displayname'] if 'displayname' in row['content'] else None
        avatar_url = row['content']['avatar_url'] if 'avatar_url' in row['content'] else None
    
       

