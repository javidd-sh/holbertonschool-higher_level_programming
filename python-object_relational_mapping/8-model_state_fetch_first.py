#!/usr/bin/python3
"""Print the first State object from the database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Connect to the database and fetch the first state"""
    if len(sys.argv) != 4:
        return

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost/{db_name}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the first State object by id
    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    main()
