import sqlite3 as lite


def create_database(database_path: str):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        cur.execute("drop table if exists words")
        ddl = "create table words (word text not null primary key,usage_count int default 1 not null);"
        cur.execute(ddl)
        ddl = "create unique index words_word_uindex on words (word);"
        cur.execute(ddl)
    conn.close()


def save_words_to_database(database_path: str, words_list: list):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        for word in words_list:
            # بررسی اینکه آیا کلمه از قبل در بانک موجود است یا خیر
            sql = "select count(word) from words where word='" + word + "'"
            count = cur.execute(sql)
            count = cur.fetchone()[0]
            if count > 0:
                sql = "update words set usage_count = usage_count+1 where  word='" + word + "'"
                cur.execute(sql)
            else:
                sql = "insert into words(word,usage_count) values ('" + word + "',1)"
                cur.execute(sql)
        #conn.close()
        print("DataBase Save Complate!")
