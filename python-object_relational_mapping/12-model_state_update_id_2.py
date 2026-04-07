#!/usr/bin/python3
"""Change the name of a State object in the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Update the name of the State with id=2 to 'New Mexico'"""
    if len(sys.argv) != 4:
        return

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, password, db_name),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "__main__":
    main()
