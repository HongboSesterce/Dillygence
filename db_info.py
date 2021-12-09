#%%
import sqlite3
import pandas as pd

# %% see what tables are in the db
con=sqlite3.connect('./data/sandbox.db')
cur=con.cursor()
table=pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table'", con)
table

# %% see what columns are in table- -
cur.execute("SELECT * FROM DF109BFD_Buffers ")
col_name_list=[tuple[0] for tuple in cur.description]
print(col_name_list)
cur.execute("SELECT * FROM DF109BFD_Buffers")
print(cur.fetchmany(2))
# %%
cur.execute("SELECT * FROM DF109BFD_Events ")
col_name_list=[tuple[0] for tuple in cur.description]
print(col_name_list)
cur.execute("SELECT * FROM DF109BFD_Events")
print(cur.fetchone())


# %%
cur.execute("SELECT * FROM DF109BFD_Exits ")
col_name_list=[tuple[0] for tuple in cur.description]
print(col_name_list)
cur.execute("SELECT * FROM DF109BFD_Exits")
print(cur.fetchmany(2))
# %%
cur.execute("SELECT * FROM DF109BFD_Teams ")
col_name_list=[tuple[0] for tuple in cur.description]
print(col_name_list)
cur.execute("SELECT * FROM DF109BFD_Teams")
print(cur.fetchmany(2))
# %% Only one
cur.execute("SELECT * FROM DF109BFD_Buffers WHERE module='AP4_PLTFTAC0432_F'")
print(cur.fetchone())
# %%
cur.execute("SELECT * FROM DF109BFD_Buffers WHERE team='E1'")
print(cur.fetchone())
# %%
