#!/usr/bin/python3
"""
module to get all states containing letter a
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    user = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]

    eng_txt = 'mysql+mysqldb://{}:{}@localhost/{}'.format(user, pwd, db_name)
    engine = create_engine(eng_txt, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    A_states = session.query(State).\
        filter(State.name.like('%a%')).order_by(State.id).all()
    for state in A_states:
        print("{}: {}".format(state.id, state.name))
