import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("evos.db")
        self.cursor = self.connection.cursor()

    def create_user_table(self):
        self.cursor.execute("""
            create table if not exists users(
            id integer primary key,
            first_name varchar(55) not null,
            last_name varchar(55),
            age integer,
            address varchar(255),
            telegram_id integer not null unique,
            lang varchar(55) default 'uz'
            )
        """)

    def get_user(self, telegram_id):
        user = self.cursor.execute("""
        select * from users where telegram_id = ?
        """, (telegram_id,)).fetchone()
        return user if user else None

    def insert_user(self, first_name, last_name, telegram_id):
        self.cursor.execute("""
        insert into users(first_name, last_name, telegram_id)
        values (?, ?, ?)
        """, (first_name, last_name, telegram_id))
        self.connection.commit()


    def get_user_lang(self, telegram_id):
        lang = self.cursor.execute("""
        select lang from users where telegram_id = ?
        """, (telegram_id,)).fetchone()
        return lang[0] if lang else "uz"
    def set_user_lang(self, telegram_id, lang):
        self.cursor.execute("""
        update users set lang = ? where telegram_id = ?
        """, (lang, telegram_id))
        self.connection.commit()


database = Database()
database.create_user_table()
