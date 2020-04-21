from sqlalchemy import Column, UnicodeText, LargeBinary, Numeric
from sql_helpers import SESSION, BASE


class LydiaAI(BASE):
    __tablename__ = "lydia_ai"
    
    chat_id = Column(Numeric, primary_key=True)
    session_id = Column(UnicodeText)
    session_expires = Column(Numeric)

    def __init__(
        self,
        
        chat_id,
        session_id,
        session_expires
    ):
        
        self.chat_id = chat_id
        self.session_id = session_id
        self.session_expires = session_expires


LydiaAI.__table__.create(checkfirst=True)


def get_s(chat_id):
    try:
        return SESSION.query(LydiaAI).get((user_id, chat_id))
    except:
        return None
    finally:
        SESSION.close()


def get_all_s():
    try:
        return SESSION.query(LydiaAI).all()
    except:
        return None
    finally:
        SESSION.close()


def add_s(
    
    chat_id,
    session_id,
    session_expires
):
    adder = SESSION.query(LydiaAI).get((user_id, chat_id))
    if adder:
        adder.session_id = session_id
        adder.session_expires = session_expires
    else:
        adder = LydiaAI(
            
            chat_id,
            session_id,
            session_expires
        )
    SESSION.add(adder)
    SESSION.commit()


def remove_s(
    
    chat_id
):
    note = SESSION.query(LydiaAI).get((user_id, chat_id))
    if note:
        SESSION.delete(note)
        SESSION.commit()
