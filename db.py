import psycopg2
from schemas import SignUpDetails

conn = psycopg2.connect(
    "dbname=mydb user=postgres password=mysecretpassword")
cur = conn.cursor()


def create_user(user: SignUpDetails):
    cur.execute("INSERT INTO user_table (user_id, email, password, created_on) VALUES (%s, %s)",
                (100, "abc'def"))
    print("Data inserted")


def fetchdata():
    cur.execute("SELECT * FROM test;")
    print(cur.fetchone())


conn.commit()

cur.close()
conn.close()
