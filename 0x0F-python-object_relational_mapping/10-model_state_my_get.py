#!/usr/bin/python3
"""
module to get state id of a state
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    user = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    eng_txt = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user, pwd, db_name)
    engine = create_engine(eng_txt, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        my_st = session.query(State).filter(State.name == state_name).first()
        print(my_st.id)
    except Exception:
        print('Not found')
