import sqlite3
con=sqlite3.connect("data.db")
import random

def check_user(ids):
    cur=con.execute(f"SELECT id FROM users_data WHERE id={ids}")
    info=cur.fetchone()
    return info
def user_add(ids,username,fullname,phone,date=None,result=0,certificate=None):
    cur=con.execute(f"SELECT id FROM users_data WHERE id={ids}")
    info=cur.fetchone()
    if info is None:
        con.execute(F"""INSERT INTO users_data (id,username,fullname,phone,result,certificate,date)\
          VALUES (?,?,?,?,?,?,?);""",(ids,username,fullname,phone,result,certificate,date))
        con.commit()

def result_info(ids):
    cur=con.execute(f"SELECT fullname,result,certificate,date FROM users_data WHERE id={ids}")
    info=cur.fetchone()
    return info

def top_results():
    cur=con.execute(f"SELECT fullname,result FROM users_data ORDER BY result DESC;")
    info=cur.fetchall()
    return info[:10]
