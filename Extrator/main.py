from models.event_json import event_json
from models.event import events
from core.configs import session


if __name__ == "__main__":
    events()
    event_json()
    session.close()


