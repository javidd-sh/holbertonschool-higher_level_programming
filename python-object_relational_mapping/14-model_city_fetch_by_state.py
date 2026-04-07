#!/usr/bin/python3
"""List all City objects from hbtn_0e_14_usa in a specific format"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    """Fetch and print cities with state name"""
    if len(sys.argv) != 4:
        return

    user, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(user, password, db_name),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities joined with their states
    cities = session.query(City).join(State).order_by(City.id).all()

    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()


if __name__ == "__main__":
    main()
