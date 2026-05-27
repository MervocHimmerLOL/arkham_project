from sqlalchemy import insert, select, and_, delete, distinct
from db.database import engine

def get_detectives(detective_table):
    with engine.connect() as conn:
        cmd = select(detective_table.c.name, detective_table.c.clues_count)
        res = conn.execute(cmd).fetchall()
    return [
        {
            'detective name': f'{row.name} ',
            'clue count': f'{row.clues_count}'
        }
        for row in res
    ]

def get_locations(location_table):
    with engine.connect() as conn:
        cmd = select(location_table.c.name)
        res = conn.execute(cmd).fetchall()
        return [
            {
                'location': f'{location.name}'
            }
            for location in res
        ]

def insert_detective(detective_table, detective_name, clue_count, cur_location):
    with engine.connect() as conn:
        cmd = select(detective_table.c.name).where(detective_table.c.name == detective_name)
        res = conn.execute(cmd).fetchone()
        if res:
            raise Exception(f"Детектив {detective_name} уже существует")
        else:
            conn.execute(insert(detective_table).values(name=detective_name, clues_count=clue_count, current_location_id=cur_location))
        conn.commit()