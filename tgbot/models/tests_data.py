import sqlite3
con=sqlite3.connect("data.db")

def test_add(title,photo,keys,date):
     con.execute(F"""INSERT INTO tests_data (title,photo,keyA,keyB,keyC,keyD,add_date)\
         VALUES ('{title}','{photo}','{keys[0]}','{keys[1]}','{keys[2]}','{keys[3]}','{date}')""")
     con.commit()
     cur=con.execute("SELECT id FROM tests_data")
     ids=cur.fetchone()
     if ids is None:
          return 1 
     return ids[0]+1

def test_info(ids):
     cur=con.execute(f"SELECT * FROM tests_data WHERE id={ids}")
     info=cur.fetchone()
     return info

def test_delete(ids):
     con.execute(f"""DELETE FROM tests_data WHERE id={ids}""")
     con.commit()
