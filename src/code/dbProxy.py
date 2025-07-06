import sqlite3


class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute("""
            create table if not exists dados(
            id integer primary key autoincrement,
            name text not null,
            score integer not null,
            date text not null
            )
            """)

    def save(self, score_dict: dict[str, int | str]):
        self.connection.execute(
            "insert into dados(name, score, date) values(:name, :score, :date)",
            score_dict,
        )
        self.connection.commit()

    def retrieve_top10(self) -> list:
        return self.connection.execute(
            "select * from dados order by score desc limit 10"
        ).fetchall()

    def close(self):
        return self.connection.close()
