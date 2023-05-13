import sqlite3
con=sqlite3.connect("data.db")
import random

def type_add(type_,start=0):
     cur=con.execute(f"SELECT name FROM tests_type WHERE name=(?)",(type_,))
     check=cur.fetchone()
     if check is None:
          con.execute(f"""INSERT INTO tests_type (name,start) VALUES (?,?);""",(type_,start,))
          con.commit()
     
def select_all_type():
     ret=[]
     cur=con.execute(f"SELECT name FROM tests_type")
     for r in cur.fetchall():
          ret.append(r[0])
     return ret

def test_add(title,photo,keys,type_,date):
     con.execute(F"""INSERT INTO tests_data (title,photo,keyA,keyB,keyC,keyD,type,add_date)\
          VALUES (?,?,?,?,?,?,?,?);""",(title,photo,keys[0],keys[1],keys[2],keys[3],type_,date))
     con.commit()
def get_test_id():
     cur=con.execute("SELECT seq FROM sqlite_sequence")
     ids=cur.fetchone()
     if ids is None:
          return 1 
     return ids[0]

def test_info(ids):
     cur=con.execute(f"SELECT * FROM tests_data WHERE id={ids}")
     info=cur.fetchone()
     return info

def test_delete(ids):
     con.execute(f"""DELETE FROM tests_data WHERE id={ids}""")
     con.commit()

def check_start_test():
     cur=con.execute("SELECT name FROM tests_type WHERE start=1")
     start=cur.fetchone()
     return start

def get_tests(types):
     cur=con.execute(f"SELECT * FROM tests_data WHERE type=(?)",(types,))
     info=list(cur.fetchall())
     random.shuffle(info)
     return info

def update_start_test(name):
     con.execute("UPDATE tests_type SET start=1 WHERE name=(?)",(name,))
     con.commit()

def restart_test():
     con.execute("UPDATE tests_type SET start=0")
     con.commit()

def tests_count():
     info=[]
     data=["users_data","tests_data","tests_type"]
     for d in data:
          cur=con.execute(f"SELECT COUNT(*) FROM {d}")
          info.append(cur.fetchone()[0])   
     return info  
     
# print(tests_count())
# print(get_tests()[0][3:7])
# from datetime import datetime
# today=datetime.today()
# end_time=datetime(today.year,today.month,today.day,today.hour+1,today.minute)

