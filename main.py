from db.database import SessionLocal
from db.models import Location, Detective
from db.db_methods import insert_detective
from sqlalchemy import Table

from db import database, db_methods

session = SessionLocal()
detectives_table = Table('Detective', database.metadata_obj, autoload_with=database.engine)
# Создаём два места

# p1 = Location(name="New Orlean")
# p2 = Location(name="Hopkins")
# session.add_all([p1, p2])
# session.commit()

# Связываем
# p1.next = p2
# session.commit()

# Создаём персонажа
# char = Detective(name="James Murdock", current_location=p1)
# session.add(char)
# session.commit()

# Проверяем
# print(char.name)
# print(char.current_location.name)        # → A
# print(char.current_location.next.name)   # → B
insert_detective(detectives_table, 'James Murdocck', 0, cur_location=0)

session.close()